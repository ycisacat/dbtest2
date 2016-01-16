$(document).ready(function(){
   var chart = {
       // plotBackgroundColor: null,
       // plotBorderWidth: null,
       // plotShadow: false
      backgroundColor: 'rgba(255, 255, 255, 0)',
      plotBorderColor : null,
      plotBackgroundColor: null,
      plotBackgroundImage:null,
      plotBorderWidth: null,
      plotShadow: false,  

   };
   var title = {
      text: ''   
   };      
   var tooltip = {
      pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
   };
   var plotOptions = {
      pie: {
         allowPointSelect: false,//控制圆环图是否裂开
         size:94,
         innerSize:72,
         cursor: 'pointer',
         dataLabels: {
            enabled: false,
            format: '<b>{point.name}%</b>: {point.percentage:.1f} %',
            style: {
               color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
            }
         }
      }
   };


    var series= [{
      type: 'pie',
      name: '占比',
      data: [
         ['悲伤',12],
         ['愤怒',22],
         ['焦虑',32],
         ['同情',42],
         ['喜欢',52],
         ['厌恶',62],
         ['愉快',72],
         ['厌恨',82]
      ]
   }];

   var json = {};
   json.chart = chart;
   json.title = title;
   json.tooltip = tooltip;
   json.series = series;
   json.plotOptions = plotOptions;
   $('#oPie3').highcharts(json);
});

                  