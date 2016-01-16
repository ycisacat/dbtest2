# coding=utf-8
__author__ = 'gu'
from sina.test_qdexchange import *
def draw_homepage_line(file_name):
    file = open(file_name,'w')
    file.write(
        """
 $(document).ready(function()
            {
              var chart =
              {
                      backgroundColor: 'rgba(0,0,0,0)',
                      type: 'line',
              };


              var title =
                {
                  text: ''  ,
                  x: -20
                  };

              var subtitle =
                {

                  x: -20,
                  style:{
                     color:"#ffffff",
                  }

                };

              var plotOptions=
              {
                  series: {
                      marker: {
                            radius: 4,
                            symbol: 'circle'
                      },
                      cursor: 'pointer'
                  }
              };

              var xAxis =
                {
                  lineColor:'rgba(0,0,0,0)',
                  categories: ['1月', '2月', '3月', '4月', '5月','6月','7月','8月','9月','10月','11月','12月'],
                  tickWidth:0,
                  plotLines:
                    [{value: 0,
                    width: 0,
                    color: '#ffffff'
                  }],
                  labels: {
                    style: {
                      color: '#ffffff',
                      fontSize:'12px'
                    }
                  },

                };
              var yAxis =
              {
                gridLineWidth:0,
                title:
                  {
                    text: '社区数： (个)',
                    style:{
                    color:"#ffffff",
                  }
              },

                plotLines:
                [{
                    value: 0,
                    width: 0,
                    color: '#ffffff'

                }],
                labels: {
                    y: 20,
                    style: {
                      color: '#ffffff',
                      fontSize:'12px'
                    }
                },
            };

            var tooltip =
            {
                valueSuffix: '个'
            }

            var legend = {
                  layout: 'vertical',
                  align: 'right',
                  verticalAlign: 'middle',
                  borderWidth: 0,
                  borderRadius:1,
                  borderColor:'#ffffff',
                  itemStyle : {
                     'color': '#ffffff'
                  },
               }

             var series = [

            {
               type:'spline',
               name: '悲伤',
               data:"""+str(home_line()[0])+"""
            },

            {
               type:'spline',
               name: '愤怒',
               data: """+str(home_line()[1])+"""
            },

            {
               type:'spline',
               name: '焦虑',
               data: """+str(home_line()[2])+"""
            },

            {
               type:'spline',
               name: '同情',
               data: """+str(home_line()[3])+"""
            },

            {
               type:'spline',
               name: '喜欢',
               data: """+str(home_line()[4])+"""
            },

            {
               type:'spline',
               name: '厌恶',
               data: """+str(home_line()[5])+"""
            },

            {
               type:'spline',
               name: '愉快',
               data: """+str(home_line()[6])+"""
            },

            {
               type:'spline',
               name: '厌恨',
               data: """+str(home_line()[7])+"""
            }];

            Highcharts.setOptions({
               credits: { enabled: false }
            })
            Highcharts.setOptions({
                colors: ['#FF9966','#FF6666', '#FFCCCC', '#FFFF99', '#CCCCFF', '#CCFFFF',
               '#d48efd', '#9ca7c7']
               // FF6666,

            });
            Highcharts.setOptions({
                colors: ['#FF9966','#FF6666', '#FFCCCC', '#FFFF99', '#CCCCFF', '#CCFFFF',
               '#d48efd', '#9ca7c7']
               // FF6666,

            });
             var json = {};
             json.chart=chart;
             json.title = title;
             json.subtitle = subtitle;
             json.plotOptions = plotOptions;
             json.xAxis = xAxis;
             json.yAxis = yAxis;
             json.tooltip = tooltip;
             json.legend = legend;
             json.series = series;

             $('#linechart').highcharts(json);
         });
                          """
    )

    file.close()
    print 'Done homepage_linechart'
# draw_home_line('/home/gu/PycharmProjects/dbtest2/static/drawjs/home_line.js')
