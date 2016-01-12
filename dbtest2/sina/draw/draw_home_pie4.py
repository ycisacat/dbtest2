# coding=utf-8
__author__ = 'gu'
from sina.exercise import *
def draw_pie4():
    infile = open('/home/yc/PycharmProjects/dbtest2/sina/draw/home_pie_common.txt','r')
    outfile = open('/home/yc/PycharmProjects/dbtest2/static/drawjs/homepage_pie4.js','w+')
    outfile.write(infile.read()+'\n'+
                  """
                  var series= [{
      type: 'pie',
      name: '占比',
      data: [
         ['快乐',"""+home_pie4()[0]+"""],
         ['喜悦',"""+home_pie4()[1]+"""],
         ['惊讶',"""+home_pie4()[2]+"""],
         ['一般',"""+home_pie4()[3]+"""],
         ['无奈',"""+home_pie4()[4]+"""],
         ['难过',"""+home_pie4()[5]+"""],
         ['愤怒',"""+home_pie4()[6]+"""],
         ['恶心',"""+home_pie4()[7]+"""]
      ]
   }];

   var json = {};
   json.chart = chart;
   json.title = title;
   json.tooltip = tooltip;
   json.series = series;
   json.plotOptions = plotOptions;
   $('#oPie4').highcharts(json);
});

                  """


                  )

    infile.close()
    outfile.close()
    print 'Done home_pie4'

# draw_pie4()