# coding=utf-8
__author__ = 'gu'
from sina.test_qdexchange import *
import draw_alljs

def draw_events1(file_name):
    outfile = open(file_name, 'w+')
    outfile.write(
    """
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>具体事件</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0">
	<script src="../static/js/jquery-1.10.1.min.js"></script>
	<script language="JavaScript" src="../static/js/login_sigin.js"></script>
	<link rel="stylesheet" href="../static/css/frame.css" />
	<link rel="stylesheet" href="../static/css/eventspage.css" />
	<link rel="stylesheet" href="../static/css/login_sigin.css" />
</head>
<body>
	<div id="head">
		<div id="headWrapper">
			<a href="index.html"><div id="logo"><img src="../static/image1/logo.png"></div></a>
			<div id="log_sig">
				<div id="btnLogin"><img src="../static/image1/login.png"></div>
				<div id="btnSigin"><img src="../static/image1/sigin.png"></div>
			</div>
		</div>
	</div>
	<HR  width="980" color=#fff SIZE=2>
	<div id="container">
		<div id="left">
			<div id="button1"><img src="../static/image2/yukuai.png"></div>
			<a href="chartspage.html"><div id="button2"></div></a>
			<a href="keywordspage.html"><div id="button3"></div></a>
			<a href="#"><div id="button4"></div></a>
			<a href="#"><div id="button5"></div></a>
			<a href="#"><div id="button6"></div></a>
			<a href="#"><div id="button7"></div></a>
			<div id="triangle"><img src="../static/image2/triangle.png"></div>
		</div>
		<div id="right">
			<div id="subtitle"><img src="../static/image2/subtitle.png" alt=""></div>
			<div id="events" >
				<table class="tablebox">
					<tbody id="table2">

	""")

    outfile.close()
    # print "event1 done"


def draw_events2(file_name):
    events_list=[]
    infile = open(draw_alljs.draw_base_dir()+'/sina/draw/eventsspage1.txt','r')
    for i in xrange(0,len(events())):
        events_list.append( """
                            <tr>
							<td id='f1'>"""+str((int(i)+1))+"""</td>
							<td id="a"><a href='#'>"""+events()[i]+"""</a></td>
						</tr>""")

    outfile = open(file_name,'w+')
    for j in events_list:
        outfile.write(infile.read()+j+'\n')
    outfile.close()
    # print "evevts2 done"




def draw_eventspage(file_name):
    draw_events1(draw_alljs.draw_base_dir()+'/sina/draw/eventsspage1.txt')
    draw_events2(draw_alljs.draw_base_dir()+'/sina/draw/eventsspage2.txt')
    infile = open(draw_alljs.draw_base_dir()+'/sina/draw/eventsspage2.txt','r')
    outfile = open(file_name, 'w+')
    outfile.write(infile.read()+
    """
				</tbody>
	        </table>
			<div id="sp">
				<span id="ye">页</span>
				<span id="spanTotalPage"></span>
				<span id="yegong">页/共</span>
				<span id="spanPageNum"></span>
				<span id="di">第</span>
				<span id="spanLast">最后一页</span><!-- </br> -->
				<span id="spanNext">下一页</span>
				<span id="spanPre">上一页</span>
				<span id="spanFirst">第一页</span>
			</div>
			<script language="JavaScript" src="../static/js/eventspage.js"></script>
			</div>
		</div>
	</div>
	<div id="footer">
		<div id="line_bottom"><HR  width="880" color=#fff SIZE=2></div>
		<div id="copyright"><p>Copyright©2015 广外舆情项目小组</p><div>
	</div>
</body>
</html>

    """
    )

    outfile.close()
    print "done eventspage.html"

