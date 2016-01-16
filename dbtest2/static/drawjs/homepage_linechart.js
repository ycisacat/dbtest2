
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
               data:[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            },

            {
               type:'spline',
               name: '愤怒',
               data: [16, 22, 18, 12, 11, 8, 6, 8, 22, 11, 23, 26]
            },

            {
               type:'spline',
               name: '焦虑',
               data: [13, 18, 26, 22, 17, 11, 16, 22, 18, 12, 11, 8]
            },

            {
               type:'spline',
               name: '同情',
               data: [6, 11, 18, 24, 15, 12, 26, 22, 17, 11, 16, 22]
            },

            {
               type:'spline',
               name: '喜欢',
               data: [2, 4.0, 7.9, 13.8, 11, 18, 24, 15, 12, 26, 17.2, 14.8]
            },

            {
               type:'spline',
               name: '厌恶',
               data: [-1.4, 2.5, 5.8, 2, 4.0, 7.9, 13.8, 11, 9.2, 15.9, 22.7, 22]
            },

            {
               type:'spline',
               name: '愉快',
               data: [-3.7, -0.8, 2.9, -1.4, 2.5, 5.8, 2, 4.0, 7.6, 14.8, 22.3, 11]
            },

            {
               type:'spline',
               name: '厌恨',
               data: [0.6, 2.2, -3.7, -0.8, 2.9, -1.4, 2.5, 5.8, 5.9, 9.7, 15.8, 17.7]
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
                          