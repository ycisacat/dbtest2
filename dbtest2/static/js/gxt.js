require.config({
        packages:[
        {
            name:'echarts',
            location:'./echarts/src',
            main:'echarts'
        },
        
        {
            name:'zrender',
            location:'./zrender/src',
            main:'zrender'
        }
        ]
    });
    var  option = {
    isShowScrollBar:false,
    series: [
        {
            type:'kforce',
            categories : [
                {
                    name: '核心',
                    itemStyle: {
                        normal: {
                            color : '#98FB98'
                        }
                    }
                },
                {
                    name:'相关',
                    itemStyle: {
                        normal: {
                            color : '#97FFFF'
                        }
                    }
                }
            ],
            itemStyle: {
                normal: {
                    label: {
                        show: true,
                        textStyle: {
                            color: '#9A32CD'
                        }
                    },
                    nodeStyle : {
                        brushType : 'both',
                        strokeColor : 'rgba(255,215,255,1)',
                        lineWidth : 2
                    }
                },emphasis:{
                    linkStyle : { strokeColor : 'red'}
                }
            },
            minRadius : 15,
            maxRadius : 20,
            density : 0.6,
            attractiveness: 0.77,
            nodes:[
               {category:0, name: '燕芬师姐', value : 10,shapeType:'rectangle',
              
             },
                {category:1, name: '文达',value : 0
            },
                {category:1, name: '冰艳',value : 0},
                {category:1, name: '洪伟',value : 0},
                {category:1, name: '嘉琳',value : 0},
                {category:1, name: '稷旗',value : 0},
                {category:1, name: '才良',value : 0},
               
            ],
            links : [
                {source : 1, target : 0, weight : 2,
                onclick:function(params){
                     alert(params.target.style.text);
                },
            },
                {source : 2, target : 0, weight : 2},
                {source : 3, target : 0, weight : 2},
                {source : 4, target : 0, weight : 2},
                {source : 5, target : 0, weight : 2},
                {source : 6, target : 0, weight : 2}
                
            ]
        }
    ]
};
require(
    [
        'echarts',
        'echarts/chart/kforce',
    ],
    function(ec) {
        var myChart = ec.init(document.getElementById('ttt'));
        myChart.setOption(option);
    }
)