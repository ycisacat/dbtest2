# coding=utf-8
__author__ = 'gu'
from sina.test_qdexchange import *
def draw_chartspage_pie(file_name):
    file = open(file_name,'w')
    file.write(
        """
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
         ['悲伤',"""+pie_data()[0]+"""],
         ['愤怒',"""+pie_data()[1]+"""],
         ['焦虑',"""+pie_data()[2]+"""],
         {
            name: '同情',
            y: """+pie_data()[3]+""",
            sliced: false,
            selected: false
         },
         ['喜欢',"""+pie_data()[4]+"""],
         ['厌恶',"""+pie_data()[5]+"""],
         ['愉快',"""+pie_data()[6]+"""],
         ['厌恨',"""+pie_data()[7]+"""]
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

        """
    )
    file.close()
    print 'Done chartspage_piechart'

# draw_pie('/home/gu/PycharmProjects/dbtest2/static/drawjs/pie.js')



