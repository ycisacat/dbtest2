# coding=utf-8
__author__ = 'gu'
from sina.test_qdexchange import *
import draw_alljs
def draw_homepage_pie5(file_name):
    infile = open(draw_alljs.draw_base_dir()+'/sina/draw/home_pie_common.txt','r')
    outfile = open(file_name,'w+')
    outfile.write(infile.read()+'\n'+
                  """
    var series= [{
      type: 'pie',
      name: '占比',
      data: [
         ['悲伤',"""+home_pie5()[0]+"""],
         ['愤怒',"""+home_pie5()[1]+"""],
         ['焦虑',"""+home_pie5()[2]+"""],
         ['同情',"""+home_pie5()[3]+"""],
         ['喜欢',"""+home_pie5()[4]+"""],
         ['厌恶',"""+home_pie5()[5]+"""],
         ['愉快',"""+home_pie5()[6]+"""],
         ['厌恨',"""+home_pie5()[7]+"""]
      ]
   }];

   var json = {};
   json.chart = chart;
   json.title = title;
   json.tooltip = tooltip;
   json.series = series;
   json.plotOptions = plotOptions;
   $('#oPie6').highcharts(json);
});

                  """


                  )

    infile.close()
    outfile.close()
    print 'Done homepage_pie5'

# draw_pie5()