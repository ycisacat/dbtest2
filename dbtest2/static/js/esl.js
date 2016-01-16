var define;
var require;

(function ( global ) {
    var modModules = {};

    var MODULE_STATE_PRE_DEFINED = 1;
    var MODULE_STATE_PRE_ANALYZED = 2;
    var MODULE_STATE_ANALYZED = 3;
    var MODULE_STATE_READY = 4;
    var MODULE_STATE_DEFINED = 5;
    var actualGlobalRequire = createLocalRequire( '' );
    var waitTimeout;
    function require( requireId, callback ) {
        assertNotContainRelativeId( requireId );
        var timeout = requireConf.waitSeconds;
        if ( isArray( requireId ) && timeout ) {
            if ( waitTimeout ) {
                clearTimeout( waitTimeout );
            }
            waitTimeout = setTimeout( waitTimeoutNotice, timeout * 1000 );
        }

        return actualGlobalRequire( requireId, callback );
    }
    require.toUrl = toUrl;
    function waitTimeoutNotice() {
        var hangModules = [];
        var missModules = [];
        var missModulesMap = {};
        var hasError;

        for ( var id in modModules ) {
            if ( !modIsDefined( id ) ) {
                hangModules.push( id );
                hasError = 1;
            }

            each(
                modModules[ id ].realDeps || [],
                function ( depId ) {
                    if ( !modModules[ depId ] && !missModulesMap[ depId ] ) {
                        hasError = 1;
                        missModules.push( depId );
                        missModulesMap[ depId ] = 1;
                    }
                }
            );
        }

        if ( hasError ) {
            throw new Error( '[MODULE_TIMEOUT]Hang( ' 
                + ( hangModules.join( ', ' ) || 'none' )
                + ' ) Miss( '
                + ( missModules.join( ', ' ) || 'none' )
                + ' )'
            );
        }
    }
    var tryDefineTimeout;
    function define() {
        var argsLen = arguments.length;
        if ( !argsLen ) {
            return;
        }

        var id;
        var dependencies;
        var factory = arguments[ --argsLen ];

        while ( argsLen-- ) {
            var arg = arguments[ argsLen ];

            if ( isString( arg ) ) {
                id = arg;
            }
            else if ( isArray( arg ) ) {
                dependencies = arg;
            }
        }
        var opera = window.opera;

        if ( 
            !id 
            && document.attachEvent 
            && (!(opera && opera.toString() === '[object Opera]')) 
        ) {
            var currentScript = getCurrentScript();
            id = currentScript && currentScript.getAttribute('data-require-id');
        }
        dependencies = dependencies || ['require', 'exports', 'module'];
        if ( id ) {
            modPreDefine( id, dependencies, factory );
            if ( tryDefineTimeout ) {
                clearTimeout( tryDefineTimeout );
            }
            tryDefineTimeout = setTimeout( modPreAnalyse, 10 );
        }
        else {
            wait4PreDefines.push( {
                deps    : dependencies,
                factory : factory
            } );
        }
    }

    define.amd = {};
    function modGetByState( state ) {
        var modules = [];
        for ( var key in modModules ) {
            var module = modModules[ key ];
            if ( module.state == state ) {
                modules.push( module );
            }
        }

        return modules;
    }
    function moduleConfigGetter() {
        var conf = requireConf.config[ this.id ];
        if ( conf && typeof conf === 'object' ) {
            return conf;
        }

        return {};
    }
    function modPreDefine( id, dependencies, factory ) {
        if ( modExists( id ) ) {
            return;
        }

        var module = {
            id       : id,
            deps     : dependencies,
            factory  : factory,
            exports  : {},
            config   : moduleConfigGetter,
            state    : MODULE_STATE_PRE_DEFINED,
            hardDeps : {}
        };
        modModules[ id ] = module;
    }
    function modPreAnalyse() {
        var pluginModuleIds = [];
        var pluginModuleIdsMap = {};
        var modules = modGetByState( MODULE_STATE_PRE_DEFINED );

        each(
            modules,
            function ( module ) {
                var realDepends = module.deps.slice( 0 );
                module.realDeps = realDepends;
                var factory = module.factory;
                var requireRule = /require\(\s*(['"'])([^'"]+)\1\s*\)/g;
                var commentRule = /(\/\*([\s\S]*?)\*\/|([^:]|^)\/\/(.*)$)/mg;
                if ( isFunction( factory ) ) {
                    factory.toString()
                        .replace( commentRule, '' )
                        .replace( requireRule, function ( $0, $1, $2 ) {
                            realDepends.push( $2 );
                        });
                }
                each(
                    realDepends,
                    function ( dependId ) {
                        var idInfo = parseId( dependId );
                        if ( idInfo.resource ) {
                            var plugId = normalize( idInfo.module, module.id );
                            if ( !pluginModuleIdsMap[ plugId ] ) {
                                pluginModuleIds.push( plugId );
                                pluginModuleIdsMap[ plugId ] = 1;
                            }
                        }
                    }
                );

                module.state = MODULE_STATE_PRE_ANALYZED;
            }
        );

        nativeRequire( pluginModuleIds, function () {
            modAnalyse( modules );
        } );
    }
    function modAnalyse( modules ) {
        var requireModules = [];

        each(
            modules,
            function ( module ) {
                if ( module.state !== MODULE_STATE_PRE_ANALYZED ) {
                    return;
                }

                var id = module.id;
                var depends = module.deps;
                var hardDepends = module.hardDeps;
                var hardDependsCount = isFunction( module.factory )
                    ? module.factory.length
                    : 0;

                each(
                    depends,
                    function ( dependId, index ) {
                        dependId = normalize( dependId, id );
                        depends[ index ] = dependId;

                        if ( index < hardDependsCount ) {
                            hardDepends[ dependId ] = 1;
                        }
                    }
                );
                var realDepends = module.realDeps;
                var len = realDepends.length;
                var existsDepend = {};
                
                while ( len-- ) {
                    var dependId = normalize( realDepends[ len ], id );
                    if ( !dependId
                         || dependId in existsDepend
                         || dependId in BUILDIN_MODULE
                    ) {
                        realDepends.splice( len, 1 );
                    }
                    else {
                        existsDepend[ dependId ] = 1;
                        realDepends[ len ] = dependId;

                        requireModules.push( dependId );
                    }
                }

                module.realDepsIndex = existsDepend;
                module.state = MODULE_STATE_ANALYZED;

                modWaitDependenciesLoaded( module );
                modInvokeFactoryDependOn( id );
            }
        );

        nativeRequire( requireModules );
    }
    function modWaitDependenciesLoaded( module ) {
        var id = module.id;

        module.invokeFactory = invokeFactory;
        invokeFactory();
        var checkingLevel = 0;
        function checkInvokeReadyState() {
            checkingLevel++;

            var isReady = 1;
            var tryDeps = [];

            each(
                module.realDeps,
                function ( depId ) {
                    if ( !modIsAnalyzed( depId ) ) {
                        isReady = 0;
                    }
                    else if ( !modIsDefined( depId ) ) {
                        switch ( modHasCircularDependency( id, depId ) ) {
                            case CIRCULAR_DEP_UNREADY:
                            case CIRCULAR_DEP_NO:
                                isReady = 0;
                                break;
                            case CIRCULAR_DEP_YES:
                                if ( module.hardDeps[ depId ] ) {
                                    tryDeps.push( depId );
                                }
                                break;
                        }
                    }
                    
                    return !!isReady;
                }
            );
            isReady && each(
                tryDeps,
                function ( depId ) {
                    modTryInvokeFactory( depId );
                }
            );

            isReady = isReady && tryDeps.length === 0;
            isReady && (module.state = MODULE_STATE_READY);

            checkingLevel--;
            return isReady;
        }
        function invokeFactory() {
            if ( module.state == MODULE_STATE_DEFINED 
                || checkingLevel > 1
                || !checkInvokeReadyState()
            ) {
                return;
            }
            try {
                var factory = module.factory;
                var exports = isFunction( factory )
                    ? factory.apply( 
                        global, 
                        modGetModulesExports( 
                            module.deps, 
                            {
                                require : createLocalRequire( id ),
                                exports : module.exports,
                                module  : module
                            } 
                        ) 
                    )
                    : factory;

                if ( typeof exports != 'undefined' ) {
                    module.exports = exports;
                }

                module.state = MODULE_STATE_DEFINED;
                module.invokeFactory = null;
            } 
            catch ( ex ) {
                if ( /^\[MODULE_MISS\]"([^"]+)/.test( ex.message ) ) {
                    module.hardDeps[ RegExp.$1 ] = 1;
                    return;
                }

                throw ex;
            }
            
            
            modInvokeFactoryDependOn( id );
            modFireDefined( id );
        }
    }
    function modGetModulesExports( modules, buildinModules ) {
        var args = [];
        each( 
            modules,
            function ( moduleId, index ) {
                args[ index ] = 
                    buildinModules[ moduleId ]
                    || modGetModuleExports( moduleId );
            } 
        );

        return args;
    }

    var CIRCULAR_DEP_UNREADY = 0;
    var CIRCULAR_DEP_NO = 1;
    var CIRCULAR_DEP_YES = 2;
    function modHasCircularDependency( source, target, meet ) {
        if ( !modIsAnalyzed( target ) ) {
            return CIRCULAR_DEP_UNREADY;
        }

        meet = meet || {};
        meet[ target ] = 1;
        
        if ( target == source ) {
            return CIRCULAR_DEP_YES;
        }

        var module = modGetModule( target );
        var depends = module && module.realDeps;
        
        
        if ( depends ) {
            var len = depends.length;

            while ( len-- ) {
                var dependId = depends[ len ];
                if ( meet[ dependId ] ) { 
                    continue;
                }

                var state = modHasCircularDependency( source, dependId, meet );
                switch ( state ) {
                    case CIRCULAR_DEP_UNREADY:
                    case CIRCULAR_DEP_YES:
                        return state;
                }
            }
        }

        return CIRCULAR_DEP_NO;
    }
    function modInvokeFactoryDependOn( id ) {
        for ( var key in modModules ) {
            var realDeps = modModules[ key ].realDepsIndex || {};
            realDeps[ id ] && modTryInvokeFactory( key );
        }
    }
    function modTryInvokeFactory( id ) {
        var module = modModules[ id ];

        if ( module && module.invokeFactory ) {
            module.invokeFactory();
        }
    }

    var modDefinedListener = [];

    var modRemoveListenerIndex = [];

    var modFireLevel = 0;

   
    function modFireDefined( id ) {
        modFireLevel++;
        each( 
            modDefinedListener,
            function ( listener ) {
                listener && listener( id );
            }
        );
        modFireLevel--;

        modSweepDefinedListener();
    }

   
    function modSweepDefinedListener() {
        if ( modFireLevel < 1 ) {
            modRemoveListenerIndex.sort( 
                function ( a, b ) { return b - a; } 
            );

            each( 
                modRemoveListenerIndex,
                function ( index ) {
                    modDefinedListener.splice( index, 1 );
                }
            );
            
            modRemoveListenerIndex = [];
        }
    }

    
    function modRemoveDefinedListener( listener ) {
        each(
            modDefinedListener,
            function ( item, index ) {
                if ( listener == item ) {
                    modRemoveListenerIndex.push( index );
                }
            }
        );
    }

    function modAddDefinedListener( listener ) {
        modDefinedListener.push( listener );
    }

   
    function modExists( id ) {
        return id in modModules;
    }

    function modIsDefined( id ) {
        return modExists( id ) 
            && modModules[ id ].state == MODULE_STATE_DEFINED;
    }

    function modIsAnalyzed( id ) {
        return modExists( id ) 
            && modModules[ id ].state >= MODULE_STATE_ANALYZED;
    }

   
    function modGetModuleExports( id ) {
        if ( modIsDefined( id ) ) {
            return modModules[ id ].exports;
        }

        return null;
    }

   
    function modGetModule( id ) {
        return modModules[ id ];
    }

    function modAddResource( resourceId, value ) {
        modModules[ resourceId ] = {
            exports: value || true,
            state: MODULE_STATE_DEFINED
        };

        modInvokeFactoryDependOn( resourceId );
        modFireDefined( resourceId );
    }

   
    var BUILDIN_MODULE = {
        require : require,
        exports : 1,
        module  : 1
    };

    var wait4PreDefines = [];

    
    function completePreDefine( currentId ) {
        var preDefines = wait4PreDefines.slice( 0 );

        wait4PreDefines.length = 0;
        wait4PreDefines = [];

        each(
            preDefines,
            function ( module ) {
                var id = module.id || currentId;
                modPreDefine( id, module.deps, module.factory );
            }
        );

        modPreAnalyse();
    }
    
    
    function nativeRequire( ids, callback, baseId ) {
        callback = callback || new Function();
        baseId = baseId || '';

        
        if ( isString( ids ) ) {
            if ( !modIsDefined( ids ) ) {
                throw new Error( '[MODULE_MISS]"' + ids + '" is not exists!' );
            }

            return modGetModuleExports( ids );
        }

        if ( !isArray( ids ) ) {
            return;
        }
        
        if ( ids.length === 0 ) {
            callback();
            return;
        }
        
        var isCallbackCalled = 0;
        modAddDefinedListener( tryFinishRequire );
        each(
            ids,
            function ( id ) {
                if ( id in BUILDIN_MODULE ) {
                    return;
                } 

                ( id.indexOf( '!' ) > 0 
                    ? loadResource
                    : loadModule
                )( id, baseId );
            }
        );

        tryFinishRequire();
        
        function tryFinishRequire() {
            if ( isCallbackCalled ) {
                return;
            }

            var visitedModule = {};

            function isAllInited( modules ) {
                var allInited = 1;
                each(
                    modules,
                    function ( id ) {
                        if ( visitedModule[ id ] ) {
                            return;
                        }
                        visitedModule[ id ] = 1;

                        if ( BUILDIN_MODULE[ id ] ) {
                            return;
                        }

                        if ( 
                            !modIsDefined( id ) 
                            || !isAllInited( modGetModule( id ).realDeps )
                        ) {
                            allInited = 0;
                            return false;
                        }
                    }
                );

                return allInited;
            }

           
            if ( isAllInited( ids ) ) {
                isCallbackCalled = 1;
                modRemoveDefinedListener( tryFinishRequire );

                callback.apply( 
                    global, 
                    modGetModulesExports( ids, BUILDIN_MODULE )
                );
            }
        }
    }

    
    var loadingModules = {};

    function loadModule( moduleId ) {
        if ( loadingModules[ moduleId ] ) {
            return;
        }
        
        if ( modExists( moduleId ) ) {
            modAnalyse( [ modGetModule( moduleId ) ] );
            return;
        }
        
        loadingModules[ moduleId ] = 1;

        
        var script = document.createElement( 'script' );
        script.setAttribute( 'data-require-id', moduleId );
        script.src = toUrl( moduleId ) ;
        script.async = true;
        if ( script.readyState ) {
            script.onreadystatechange = loadedListener;
        }
        else {
            script.onload = loadedListener;
        }
        appendScript( script );

        
        function loadedListener() {
            var readyState = script.readyState;
            if ( 
                typeof readyState == 'undefined'
                || /^(loaded|complete)$/.test( readyState )
            ) {
                script.onload = script.onreadystatechange = null;
                script = null;

                completePreDefine( moduleId );
                delete loadingModules[ moduleId ];
            }
        }
    }

    function loadResource( pluginAndResource, baseId ) {
        var idInfo = parseId( pluginAndResource );
        var pluginId = idInfo.module;
        var resourceId = idInfo.resource;

        
        function pluginOnload( value ) {
            modAddResource( pluginAndResource, value );
        }

       
        pluginOnload.fromText = function ( id, text ) {
            new Function( text )();
            completePreDefine( id );
        };

       
        function load( plugin ) {
            if ( !modIsDefined( pluginAndResource ) ) {
                plugin.load( 
                    resourceId, 
                    createLocalRequire( baseId ),
                    pluginOnload,
                    moduleConfigGetter.call( { id: pluginAndResource } )
                );
            }
        }

        if ( !modIsDefined( pluginId ) ) {
            nativeRequire( [ pluginId ], load ); 
        }
        else {
            load( modGetModuleExports( pluginId ) );
        }
    }

  
    var requireConf = { 
        baseUrl     : './',
        paths       : {},
        config      : {},
        map         : {},
        packages    : [],
        waitSeconds : 0,
        urlArgs     : {}
    };

    
    function mixConfig( name, value ) {
        var originValue = requireConf[ name ];
        var type = typeof originValue;
        if ( type == 'string' || type == 'number' ) {
            requireConf[ name ] = value;
        }
        else if ( isArray( originValue ) ) {
            each( value, function ( item ) {
                originValue.push( item );
            } );
        }
        else {
            for ( var key in value ) {
                originValue[ key ] = value[ key ];
            }
        }
    }

   
    require.config = function ( conf ) {
      
        for ( var key in requireConf ) {
            if ( conf.hasOwnProperty( key ) ) {
                var confItem = conf[ key ];
                if ( key == 'urlArgs' && isString( confItem ) ) {
                    defaultUrlArgs = confItem;
                }
                else {
                    mixConfig( key, confItem );
                }
            }
        }
        
        createConfIndex();
    };

    
    createConfIndex();

   
    function createConfIndex() {
        requireConf.baseUrl = requireConf.baseUrl.replace( /\/$/, '' ) + '/';
        createPathsIndex();
        createMappingIdIndex();
        createPackagesIndex();
        createUrlArgsIndex();
    }

   
    var packagesIndex;

   
    function createPackagesIndex() {
        packagesIndex = [];
        each( 
            requireConf.packages,
            function ( packageConf ) {
                var pkg = packageConf;
                if ( isString( packageConf ) ) {
                    pkg = {
                        name: packageConf.split('/')[ 0 ],
                        location: packageConf,
                        main: 'main'
                    };
                }
                
                pkg.location = pkg.location || pkg.name;
                pkg.main = (pkg.main || 'main').replace(/\.js$/i, '');
                packagesIndex.push( pkg );
            }
        );

        packagesIndex.sort( createDescSorter( 'name' ) );
    }

    var pathsIndex;

    
    function createPathsIndex() {
        pathsIndex = kv2List( requireConf.paths );
        pathsIndex.sort( createDescSorter() );
    }

    var defaultUrlArgs;

    
    var urlArgsIndex;

    function createUrlArgsIndex() {
        urlArgsIndex = kv2List( requireConf.urlArgs );
        urlArgsIndex.sort( createDescSorter() );
    }

    
    var mappingIdIndex;
    
   
    function createMappingIdIndex() {
        mappingIdIndex = [];
        
        mappingIdIndex = kv2List( requireConf.map );
        mappingIdIndex.sort( createDescSorter() );

        each(
            mappingIdIndex,
            function ( item ) {
                var key = item.k;
                item.v = kv2List( item.v );
                item.v.sort( createDescSorter() );
                item.reg = key == '*'
                    ? /^/
                    : createPrefixRegexp( key );
            }
        );
    }

    
    function toUrl( source ) {
        
        var extReg = /(\.[a-z0-9]+)$/i;
        var queryReg = /(\?[^#]*)$/i;
        var extname = '.js';
        var id = source;
        var query = '';

        if ( queryReg.test( source ) ) {
            query = RegExp.$1;
            source = source.replace( queryReg, '' );
        }

        if ( extReg.test( source ) ) {
            extname = RegExp.$1;
            id = source.replace( extReg, '' );
        }

        if ( !MODULE_ID_REG.test( id ) ) {
            return source;
        }
        
        var url = id;

        
        var isPathMap;
        each( pathsIndex, function ( item ) {
            var key = item.k;
            if ( createPrefixRegexp( key ).test( id ) ) {
                url = url.replace( key, item.v );
                isPathMap = 1;
                return false;
            }
        } );

       
        if ( !isPathMap ) {
            each( 
                packagesIndex,
                function ( packageConf ) {
                    var name = packageConf.name;
                    if ( createPrefixRegexp( name ).test( id ) ) {
                        url = url.replace( name, packageConf.location );
                        return false;
                    }
                }
            );
        }

        
        if ( !/^([a-z]{2,10}:\/)?\//i.test( url ) ) {
            url = requireConf.baseUrl + url;
        }

        
        url += extname + query;


        var isUrlArgsAppended;

      
        function appendUrlArgs( args ) {
            if ( !isUrlArgsAppended ) {
                url += ( url.indexOf( '?' ) > 0 ? '&' : '?' ) + args;
                isUrlArgsAppended = 1;
            }
        }
        
        
        each( urlArgsIndex, function ( item ) {
            if ( createPrefixRegexp( item.k ).test( id ) ) {
                appendUrlArgs( item.v );
                return false;
            }
        } );
        defaultUrlArgs && appendUrlArgs( defaultUrlArgs );

        return url;
    }

   
    function createLocalRequire( baseId ) {
        var requiredCache = {};
        function req( requireId, callback ) {
            if ( isString( requireId ) ) {
                var requiredModule;
                if ( !( requiredModule = requiredCache[ requireId ] ) ) {
                    requiredModule = nativeRequire( 
                        normalize( requireId, baseId ), 
                        callback, 
                        baseId 
                    );
                    requiredCache[ requireId ] = requiredModule;
                }
                
                return requiredModule;
            }
            else if ( isArray( requireId ) ) {
                
                var unloadedPluginModules = [];
                each( 
                    requireId, 
                    function ( id ) { 
                        var idInfo = parseId( id );
                        var pluginId = normalize( idInfo.module, baseId );
                        if ( idInfo.resource && !modIsDefined( pluginId ) ) {
                            unloadedPluginModules.push( pluginId );
                        }
                    }
                );

                
                nativeRequire( 
                    unloadedPluginModules, 
                    function () {
                        var ids = [];
                        each( 
                            requireId, 
                            function ( id ) { 
                                ids.push( normalize( id, baseId ) ); 
                            } 
                        );
                        nativeRequire( ids, callback, baseId );
                    }, 
                    baseId
                );
            }
        }

        
        req.toUrl = function ( id ) {
            return toUrl( normalize( id, baseId ) );
        };

        return req;
    }

    
    function normalize( id, baseId ) {
        if ( !id ) {
            return '';
        }

        var idInfo = parseId( id );
        if ( !idInfo ) {
            return id;
        }

        var resourceId = idInfo.resource;
        var moduleId = relative2absolute( idInfo.module, baseId );

        each(
            packagesIndex,
            function ( packageConf ) {
                var name = packageConf.name;
                var main = name + '/' + packageConf.main;
                if ( name == moduleId
                ) {
                    moduleId = moduleId.replace( name, main );
                    return false;
                }
            }
        );

        moduleId = mappingId( moduleId, baseId );
        
        if ( resourceId ) {
            var module = modGetModuleExports( moduleId );
            resourceId = module && module.normalize
                ? module.normalize( 
                    resourceId, 
                    function ( resId ) {
                        return normalize( resId, baseId );
                    }
                  )
                : normalize( resourceId, baseId );
            
            return moduleId + '!' + resourceId;
        }
        
        return moduleId;
    }

    function relative2absolute( id, baseId ) {
        if ( /^\.{1,2}/.test( id ) ) {
            var basePath = baseId.split( '/' );
            var namePath = id.split( '/' );
            var baseLen = basePath.length - 1;
            var nameLen = namePath.length;
            var cutBaseTerms = 0;
            var cutNameTerms = 0;

            pathLoop: for ( var i = 0; i < nameLen; i++ ) {
                var term = namePath[ i ];
                switch ( term ) {
                    case '..':
                        if ( cutBaseTerms < baseLen ) {
                            cutBaseTerms++;
                            cutNameTerms++;
                        }
                        else {
                            break pathLoop;
                        }
                        break;
                    case '.':
                        cutNameTerms++;
                        break;
                    default:
                        break pathLoop;
                }
            }

            basePath.length = baseLen - cutBaseTerms;
            namePath = namePath.slice( cutNameTerms );

            basePath.push.apply( basePath, namePath );
            return basePath.join( '/' );
        }

        return id;
    }

   
    function assertNotContainRelativeId( requireId ) {
        var invalidIds = [];

        
        function monitor( id ) {
            if ( /^\.{1,2}/.test( id ) ) {
                invalidIds.push( id );
            }
        }

        if ( isString( requireId ) ) {
            monitor( requireId );
        }
        else {
            each( 
                requireId, 
                function ( id ) {
                    monitor( id );
                }
            );
        }

       
        if ( invalidIds.length > 0 ) {
            throw new Error(
                '[REQUIRE_FATAL]Relative ID is not allowed in global require: ' 
                + invalidIds.join( ', ' )
            );
        }
    }

    var MODULE_ID_REG = /^[-_a-z0-9\.]+(\/[-_a-z0-9\.]+)*$/i;

   
    function parseId( id ) {
        var segs = id.split( '!' );

        if ( MODULE_ID_REG.test( segs[ 0 ] ) ) {
            return {
                module   : segs[ 0 ],
                resource : segs[ 1 ] || ''
            };
        }

        return null;
    }

    
    function mappingId( id, baseId ) {
        each( 
            mappingIdIndex, 
            function ( item ) {
                if ( item.reg.test( baseId ) ) {

                    each( item.v, function ( mapData ) {
                        var key = mapData.k;
                        var rule = createPrefixRegexp( key );
                        
                        if ( rule.test( id ) ) {
                            id = id.replace( key, mapData.v );
                            return false;
                        }
                    } );

                    return false;
                }
            }
        );

        return id;
    }

   
    function kv2List( source ) {
        var list = [];
        for ( var key in source ) {
            if ( source.hasOwnProperty( key ) ) {
                list.push( {
                    k: key, 
                    v: source[ key ]
                } );
            }
        }

        return list;
    }

    
    var currentlyAddingScript;
    var interactiveScript;

   
    function getCurrentScript() {
        if ( currentlyAddingScript ) {
            return currentlyAddingScript;
        }
        else if ( 
            interactiveScript 
            && interactiveScript.readyState == 'interactive'
        ) {
            return interactiveScript;
        }
        else {
            var scripts = document.getElementsByTagName( 'script' );
            var scriptLen = scripts.length;
            while ( scriptLen-- ) {
                var script = scripts[ scriptLen ];
                if ( script.readyState == 'interactive' ) {
                    interactiveScript = script;
                    return script;
                }
            }
        }
    }

   
    function appendScript( script ) {
        currentlyAddingScript = script;

        var doc = document;
        (doc.getElementsByTagName('head')[0] || doc.body).appendChild( script );
        
        currentlyAddingScript = null;
    }

   
    function createPrefixRegexp( prefix ) {
        return new RegExp( '^' + prefix + '(/|$)' );
    }

    function isArray( obj ) {
        return obj instanceof Array;
    }


    function isFunction( obj ) {
        return typeof obj == 'function';
    }

    
    function isString( obj ) {
        return typeof obj == 'string';
    }

    
    function each( source, iterator ) {
        if ( isArray( source ) ) {
            for ( var i = 0, len = source.length; i < len; i++ ) {
                if ( iterator( source[ i ], i ) === false ) {
                    break;
                }
            }
        }
    }

    
    function createDescSorter( property ) {
        property = property || 'k';

        return function ( a, b ) {
            var aValue = a[ property ];
            var bValue = b[ property ];

            if ( bValue == '*' ) {
                return -1;
            }

            if ( aValue == '*' ) {
                return 1;
            }

            return bValue.length - aValue.length;
        };
    }

    
    global.define = define;
    global.require = require;
})( this );
