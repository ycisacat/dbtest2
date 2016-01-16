
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
         ['悲伤',1],
         ['愤怒',2],
         ['焦虑',3],
         {
            name: '同情',
            y: 4,
            sliced: false,
            selected: false
         },
         ['喜欢',5],
         ['厌恶',6],
         ['愉快',7],
         ['厌恨',8]
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

        