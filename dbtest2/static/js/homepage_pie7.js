$(document).ready(function(){
   var chart = {
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
         allowPointSelect: true,
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
         ['快乐',29.0],
         ['喜悦',26.8],
         ['惊讶',25.7],
         ['一般',21.5],
         ['无奈',19.3],
         ['难过',17.3],
         ['愤怒',15.1],
         ['恶心',12.7]
      ]
   }];     
      
   var json = {};   
   json.chart = chart; 
   json.title = title;     
   json.tooltip = tooltip;  
   json.series = series;
   json.plotOptions = plotOptions;
   $('#oPie8').highcharts(json);
});