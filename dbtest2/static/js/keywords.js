function openNew1(){
		//获取页面的高度和宽度
		var sWidth=document.body.scrollWidth;
		var sHeight=document.body.scrollHeight;
		   	//获取页面的可视区域高度和宽度
		   	var wHeight=document.documentElement.clientHeight;
		   	var oMask=document.createElement("div");
		    	oMask.id="mask";
		      	oMask.style.height=sHeight+"px";
		      	oMask.style.width=sWidth+"px";
		      	document.body.appendChild(oMask);
		   	var oLogin=document.createElement("div");
		      	oLogin.id="login";
		      	oLogin.innerHTML="<div class='loginCon'><div id='close'></div><form><ul><li><input type='text' placeholder='用户名'></li><li><input type='password' placeholder='密码'></li><li><input type='submit' value='登录'></li></ul></form></div>";
		      document.body.appendChild(oLogin);
		   
		   	//获取登陆框的宽和高
		   	var dHeight=oLogin.offsetHeight;
		   	var dWidth=oLogin.offsetWidth;
		      	//设置登陆框的left和top
		      	oLogin.style.left=sWidth/2-dWidth/2+"px";
		      	oLogin.style.top=wHeight/2-dHeight/2+"px";
		   	//点击关闭按钮
		   	var oClose=document.getElementById("close");
		   
		      	//点击登陆框以外的区域也可以关闭登陆框
		      	oClose.onclick=oMask.onclick=function(){
		            document.body.removeChild(oLogin);
		            document.body.removeChild(oMask);
		         };
};

function openNew2(){
   	//获取页面的高度和宽度
   	var sWidth=document.body.scrollWidth;
      var sHeight=document.body.scrollHeight;
      //获取页面的可视区域高度和宽度
      var wHeight=document.documentElement.clientHeight;
      var oMask=document.createElement("div");
          oMask.id="mask1";
          oMask.style.height=sHeight+"px";
          oMask.style.width=sWidth+"px";
      document.body.appendChild(oMask);
      var oSigin=document.createElement("div");
          oSigin.id="sigin";
          oSigin.innerHTML="<div class='siginCon'><div id='close1'></div><form ><ul><li><input type='text' placeholder='用户名'></li><li><input type='password' placeholder='密码'></li><li><input type='submit' value='注册'></li></ul></form></div>";
      document.body.appendChild(oSigin);
   
      //获取登陆框的宽和高
      var dHeight=oSigin.offsetHeight;
      var dWidth=oSigin.offsetWidth;
      //设置登陆框的left和top
          oSigin.style.left=sWidth/2-dWidth/2+"px";
          oSigin.style.top=wHeight/2-dHeight/2+"px";
      //点击关闭按钮
      var oClose=document.getElementById("close1");
   
      //点击登陆框以外的区域也可以关闭登陆框
      oClose.onclick=oMask.onclick=function(){
               document.body.removeChild(oSigin);
               document.body.removeChild(oMask);
      };
};





//这里是关键字代码
var radius = 150;//控制球体的大小
var dtr = Math.PI/180;//
var d=270;//大约是控制深度，嗯，改到100效果好玩

var mcList = [];
var active = false;
var lasta = 1;
var lastb = 1;
var distr = true;
var tspeed=5;
var size=250;

var mouseX=0;
var mouseY=0;

var howElliptical=1;

var aA=null;
var oDiv=null;

window.onload=function ()
{
	var i=0;
	var oTag=null;
	oDiv=document.getElementById('tagbox');
	aA=oDiv.getElementsByTagName('a');
	for(i=0;i<aA.length;i++)
	{
		oTag={};
		
		oTag.offsetWidth=aA[i].offsetWidth;
		oTag.offsetHeight=aA[i].offsetHeight;
		
		mcList.push(oTag);
	}
	
	sineCosine( 0,0,0 );
	
	positionAll();
	
	oDiv.onmouseover=function ()
	{
		active=true;
	};
	
	oDiv.onmouseout=function ()
	{
		active=false;
	};
	
	oDiv.onmousemove=function (ev)
	{
		var oEvent=window.event || ev;
		
		mouseX=oEvent.clientX-(oDiv.offsetLeft+oDiv.offsetWidth/2);
		mouseY=oEvent.clientY-(oDiv.offsetTop+oDiv.offsetHeight/2);
		
		mouseX/=5;
		mouseY/=5;
	};
	
	setInterval(update, 120);

	var oBtn=document.getElementById("btnLogin");
      //点击登录按钮
     var oBtn1=document.getElementById("btnSigin");
      //点击登录按钮
     oBtn.onclick=function(){
            openNew1();
            return false;
      }
     oBtn1.onclick=function(){
            openNew2();
            return false;
      }   



};

function update()
{
	var a;
	var b;
	
	if(active)
	{
		a = (-Math.min( Math.max( -mouseY, -size ), size ) / radius ) * tspeed;
		b = (Math.min( Math.max( -mouseX, -size ), size ) / radius ) * tspeed;
	}
	else
	{
		a = lasta * 0.98;
		b = lastb * 0.98;
	}
	
	lasta=a;
	lastb=b;
	
	if(Math.abs(a)<=0.01 && Math.abs(b)<=0.01)
	{
		return;
	}
	
	var c=0;
	sineCosine(a,b,c);
	for(var j=0;j<mcList.length;j++)
	{
		var rx1=mcList[j].cx;
		var ry1=mcList[j].cy*ca+mcList[j].cz*(-sa);
		var rz1=mcList[j].cy*sa+mcList[j].cz*ca;
		
		var rx2=rx1*cb+rz1*sb;
		var ry2=ry1;
		var rz2=rx1*(-sb)+rz1*cb;
		
		var rx3=rx2*cc+ry2*(-sc);
		var ry3=rx2*sc+ry2*cc;
		var rz3=rz2;
		
		mcList[j].cx=rx3;
		mcList[j].cy=ry3;
		mcList[j].cz=rz3;
		
		per=d/(d+rz3);
		
		mcList[j].x=(howElliptical*rx3*per)-(howElliptical*2);
		mcList[j].y=ry3*per;
		mcList[j].scale=per;
		mcList[j].alpha=per;
		
		mcList[j].alpha=(mcList[j].alpha-0.6)*(10/6);
	}
	
	doPosition();
	depthSort();
}

function depthSort()
{
	var i=0;
	var aTmp=[];
	
	for(i=0;i<aA.length;i++)
	{
		aTmp.push(aA[i]);
	}
	
	aTmp.sort
	(
		function (vItem1, vItem2)
		{
			if(vItem1.cz>vItem2.cz)
			{
				return -1;
			}
			else if(vItem1.cz<vItem2.cz)
			{
				return 1;
			}
			else
			{
				return 0;
			}
		}
	);
	
	for(i=0;i<aTmp.length;i++)
	{
		aTmp[i].style.zIndex=i;
	}
}

function positionAll()
{
	var phi=0;
	var theta=0;
	var max=mcList.length;
	var i=0;
	
	var aTmp=[];
	var oFragment=document.createDocumentFragment();
	
	//Ëæ»úÅÅÐò
	for(i=0;i<aA.length;i++)
	{
		aTmp.push(aA[i]);
	}
	
	aTmp.sort
	(
		function ()
		{
			return Math.random()<0.5?1:-1;
		}
	);
	
	for(i=0;i<aTmp.length;i++)
	{
		oFragment.appendChild(aTmp[i]);
	}
	
	oDiv.appendChild(oFragment);
	
	for( var i=1; i<max+1; i++){
		if( distr )
		{
			phi = Math.acos(-1+(2*i-1)/max);
			theta = Math.sqrt(max*Math.PI)*phi;
		}
		else
		{
			phi = Math.random()*(Math.PI);
			theta = Math.random()*(2*Math.PI);
		}
		//×ø±ê±ä»»
		mcList[i-1].cx = radius * Math.cos(theta)*Math.sin(phi);
		mcList[i-1].cy = radius * Math.sin(theta)*Math.sin(phi);
		mcList[i-1].cz = radius * Math.cos(phi);
		
		aA[i-1].style.left=mcList[i-1].cx+oDiv.offsetWidth/2-mcList[i-1].offsetWidth/2+'px';
		aA[i-1].style.top=mcList[i-1].cy+oDiv.offsetHeight/2-mcList[i-1].offsetHeight/2+'px';
	}
}

function doPosition()
{
	var l=oDiv.offsetWidth/2;
	var t=oDiv.offsetHeight/2;
	for(var i=0;i<mcList.length;i++)
	{
		aA[i].style.left=mcList[i].cx+l-mcList[i].offsetWidth/2+'px';
		aA[i].style.top=mcList[i].cy+t-mcList[i].offsetHeight/2+'px';
		
		aA[i].style.fontSize=Math.ceil(12*mcList[i].scale/2)+8+'px';
		
		aA[i].style.filter="alpha(opacity="+100*mcList[i].alpha+")";
		aA[i].style.opacity=mcList[i].alpha;
	}
}

function sineCosine( a, b, c)
{
	sa = Math.sin(a * dtr);
	ca = Math.cos(a * dtr);
	sb = Math.sin(b * dtr);
	cb = Math.cos(b * dtr);
	sc = Math.sin(c * dtr);
	cc = Math.cos(c * dtr);
}