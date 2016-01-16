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

        data: [ {y:1,color:"#F7846B"},
                {y:2,color:"#F79C9C"},
                {y:3,color:"#FFBDA5"},
                {y:4,color:"#FFE6DE"},
                {y:5,color:"#FFFFEF"},
                {y:6,color:"#FFEFBD"},
                {y:7,color:"#D6E6B5"},
                {y:8,color:"#CEE6E6"} ]



           /* dataLabels: {
                enabled: true,
                rotation: -90,
                color: '#FFFFFF',
                align: 'right',
                format: '{point.y:.1f}', // one decimal
                y: 10, // 10 pixels down from the top
                style: {
                    fontSize: '15px',
                    fontFamily: 'Verdana, sans-serif'
                }
            }*/  //控制显示在柱状图上的数字的一系列的形态，包括显示与否，角度，样式等
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
        