# coding=utf-8
__author__ = 'gu'
from sina.test_qdexchange import *
import draw_alljs

def draw_keywords1(file_name):
    outfile = open(file_name, 'w+')
    outfile.write(
        """
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>关键字</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0">
    <script src="../static/js/jquery-1.10.1.min.js"></script>
    <link rel="stylesheet" href="../static/css/frame.css" />
    <link rel="stylesheet" href="../static/css/keywordspage.css" />
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
            <a href="#"><div id="button3"></div></a>
            <a href="eventspage.html"><div id="button4"></div></a>
            <a href="#"><div id="button5"></div></a>
            <a href="#"><div id="button6"></div></a>
            <a href="#"><div id="button7"></div></a>
            <div id="triangle"><img src="../static/image2/triangle.png"></div>
        </div>
        <div id="right">
            <div id="subtitle"><img src="../static/image2/subtitle_keywords.png" alt=""></div>
            <div id="tagbox">
            """)
    outfile.close()
    # print "done1"


def draw_keywords2(file_name):
    infile = open(draw_alljs.draw_base_dir()+'/sina/draw/keywordspage1.txt', 'r')
    outfile = open(file_name, 'w+')
    key_ws = []
    for i in xrange(0, len(key_words())):
        key_ws.append("<a href='#'>" + key_words()[i] + "</a>")
    for j in key_ws:
        # print(i)
        outfile.write(infile.read() + '\n' + j)
    outfile.close()
    # print("done2")


def draw_keywords(file_name):
    draw_keywords1(draw_alljs.draw_base_dir()+'/sina/draw/keywordspage1.txt')
    draw_keywords2(draw_alljs.draw_base_dir()+'/sina/draw/keywordspage2.txt')
    infile = open(draw_alljs.draw_base_dir()+'/sina/draw/keywordspage2.txt', 'r')
    outfile = open(file_name, 'w+')
    outfile.write(infile.read() + '\n' +
                  """
            </div>
        </div>
    </div>
    <div id="footer">
        <div id="line_bottom"><HR  width="880" color=#fff SIZE=2></div>
        <div id="copyright"><p>Copyright©2015 广外舆情项目小组</p></div>
    </div>
    <script language="JavaScript" src="../static/js/keywords.js"></script>
    <!-- 这里的keywords.js包含了login_sigin.js,请不要随意拆开，否则会有bug -->
</body>
</html>
    """)
    outfile.close()
    # print "done3"
    print "done keywordspage.html"

