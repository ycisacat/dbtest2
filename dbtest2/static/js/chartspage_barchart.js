$(document).ready(function() {  
   var chart = {
    backgroundColor: 'rgba(0,0,0,0)',
    type: 'column'
 };
   var title = {
     style:{
                     color:"#fff",},
      text: ''   
   };    
   var subtitle = {
    style:{
                     color:"#fff",},
      text: ''
   };

var credits = {
      enabled: false
   };
   var xAxis = {
      categories:['悲伤','愤怒','焦虑','同情','喜欢','厌恶','愉快','怨恨'],
      labels: {
         rotation: 0,
         style: {
            fontSize: '13px',
            fontFamily: 'Verdana, sans-serif',
            color:"#FFFFFF",
         }
      }
   };
   var yAxis ={
      min: 0,
      title: {
        text: 'Percent (%)',
          style:{color:"#fff"}
      },
      gridLineColor: '#197F07',
    gridLineWidth: 0,
     labels: {
         rotation: 0,
         style: {
            fontSize: '13px',
            fontFamily: 'Verdana, sans-serif',
            color:"#FFFFFF",
         }
      }
   };  
   var tooltip = {
      pointFormat: '情绪: <b>{point.y:.1f} %</b>'
   };   
  
   var plotOptions = {
      column: {
         
        showInLegend:false,
        cursor: 'pointer'
      }  
   };    
   var series= [{
            name: ' ',
            
                        data: [{y:23.7,color:"#FF6666"},//这些data里的y值是需要后台数据的
                {y:16.1,color:"#FF9966"}, 
                {y:7.8,color:"#FFCCCC"}, 
                               {y:18.9,color:"#FFFF99"},
                               {y:15.1,color:"#CCFFFF"}, 
                {y:18.5,color:"#CCCCFF"}, 
                               {y:27.2,color:"#9ca7c7"},
                {y:14,color:"#d48efd"}]
   }];       
   var json = {};   
   json.chart = chart; 
   json.title = title;   
   json.subtitle = subtitle;
   json.xAxis = xAxis;
   json.yAxis = yAxis; 
   json.plotOptions = plotOptions;  
   json.tooltip = tooltip;   
   json.credits = credits;
   json.series = series;
   $('#bar_chart').highcharts(json);
});