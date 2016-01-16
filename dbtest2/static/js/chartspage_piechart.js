$(document).ready(function() {  
   var chart = {
      backgroundColor: 'rgba(0,0,0,0)',
      plotBackgroundColor: null,
      plotBorderWidth: null,
      plotShadow: false,
  
   };
   var title = {
      style:{
                     color:"#fff",},
      text: ''   
   };      
   var tooltip = {
      pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
   };
   var plotOptions = {
      pie: {
         allowPointSelect: true,
         cursor: 'pointer',
         dataLabels: {
            enabled: false           
         },
         showInLegend: false
      }
   };
   Highcharts.setOptions({
credits: { enabled: false }
})
   var series= [{
      type: 'pie',
      name: '情绪',
     
    
      data: [
         // ['悲伤',500],//data里的数据需要后台的值
         {
            name:'悲伤',
            y:500,
            sliced:true,
            selected:true
         },
         ['愤怒',400],
         ['焦虑',300],
         ['同情',300],
         // {
         //    name: '同情',
         //    y: 300,
         //    sliced: true,
         //    selected: true
         // },
         ['喜欢',200],
         ['厌恶',150],
         ['愉快',50],
         ['怨恨',23]
      ]
   }];     
      
   var json = {};   
   json.chart = chart; 
   json.title = title;     
   json.tooltip = tooltip;  
   json.series = series;
   json.plotOptions = plotOptions;
   $('#pie_chart').highcharts(json);  
});