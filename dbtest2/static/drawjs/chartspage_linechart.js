
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
                            symbol: 'circle',
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
                  borderRadius:5,
                  borderColor:'#ffffff',
                  itemStyle : {
                     'color': '#ffffff'
                  },
               }

             var series = [
            {
               type:'spline',
               name: '悲伤',
               data: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            },

            {
               type:'spline',
               name: '愤怒',
               data:  [5, 9, 5, 3, 2, 49, 7, 2, 5, 14, 8, 5]
            },

            {
               type:'spline',
               name: '焦虑',
               data:  [25, 19, 5, 13, 12, 9, 7, 2, 5, 14, 8, 5]
            },

            {
               type:'spline',
               name: '同情',
               data:  [2, 19, 15, 13, 12, 9, 37, 2, 5, 14, 8, 5]
            },

            {
               type:'spline',
               name: '喜欢',
               data:  [25, 19, 1, 13, 1, 9, 7, 22, 5, 14, 8, 5]
            },

            {
               type:'spline',
               name: '厌恶',
               data:  [25, 19, 15, 13, 2, 9, 7, 22, 5, 14, 8, 5]
            },

            {
               type:'spline',
               name: '愉快',
               data:  [5, 1, 1, 13, 12, 9, 7, 2, 5, 4, 8, 5]
            },

            {
               type:'spline',
               name: '厌恨',
               data:  [0.6, 2.2, 5.9, 9.7, 15.8, 17.7, 10.8, 9.8, 7.2, 1.9, -5.1, -8.1]
            }];

            Highcharts.setOptions({
               credits: { enabled: false }
            })
            Highcharts.setOptions({
                colors: ['#FF6666','#FF9966', '#FFCCCC', '#FFFF99', '#CCCCFF', '#CCFFFF',
               '#CCCCCC', '#CCFFCC',]
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

             $('#line_chart').highcharts(json);
         });
                 