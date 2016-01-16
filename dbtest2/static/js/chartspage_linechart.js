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
               data: [25, 19, 15, 13, 12, 9,7,2,5,14,8,5]
               //这些data里的数字是需要后台的数据
            },
                                     
            {
               type:'spline',
               name: '愤怒',
               data: [16, 22, 18, 12, 11, 8,12,16,18,10,8,4]             
            }, 
                           
            {
               type:'spline',
               name: '焦虑',
               data: [13, 18, 26, 22, 17, 11,10,5,8,13,19,20]
            }, 
                         
            {
               type:'spline',
               name: '同情',
               data: [6, 11, 18, 24, 15, 12,7,4,2,1,-6,-8]              
            },
                         
            {
               type:'spline',
               name: '喜欢',
               data: [2, 4.0, 7.9, 13.8, 17.2, 14.8,16.4,18.8,13.2,10.9,12.2,15]
            },
                           
            {
               type:'spline',
               name: '厌恶',
               data: [-1.4, 2.5,5.8, 9.2, 15.9, 22.7,24,25.3,21.8,16,13.2,9.1]
            },
                           
            {
               type:'spline',
               name: '愉快',
               data: [-3.7, -0.8, 2.9, 7.6, 14.8, 22.3,17,14,8.2,10.7,14.2,11.3]
            },
                           
            {
               type:'spline',
               name: '怨恨',
               data: [0.6, 2.2,5.9, 9.7, 15.8, 17.7,10.8,9.8,7.2,1.9,-5.1,-8.1]
            }];    
                 
            Highcharts.setOptions({
               credits: { enabled: false }
            })
            Highcharts.setOptions({
                colors: ['#FF6666','#FF9966', '#FFCCCC', '#FFFF99', '#CCFFFF', '#CCCCFF',
               '#9ca7c7', '#d48efd']
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