# coding=utf-8
__author__ = 'gu'
from sina.test_qdexchange import *
import draw_alljs
def draw_homepage_pie3(file_name):
    infile = open(draw_alljs.draw_base_dir()+'/sina/draw/home_pie_common.txt','r')
    outfile = open(file_name,'w+')
    outfile.write(infile.read()+'\n'+
                  """
    var series= [{
      type: 'pie',
      name: '占比',
      data: [
         ['悲伤',"""+home_pie3()[0]+"""],
         ['愤怒',"""+home_pie3()[1]+"""],
         ['焦虑',"""+home_pie3()[2]+"""],
         ['同情',"""+home_pie3()[3]+"""],
         ['喜欢',"""+home_pie3()[4]+"""],
         ['厌恶',"""+home_pie3()[5]+"""],
         ['愉快',"""+home_pie3()[6]+"""],
         ['厌恨',"""+home_pie3()[7]+"""]
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

                  """


                  )

    infile.close()
    outfile.close()
    print 'Done homepage_pie3'

# draw_pie3()