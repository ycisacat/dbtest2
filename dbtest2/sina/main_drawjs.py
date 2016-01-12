# coding=utf-8
__author__ = 'gu'
from sina.exercise import *
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","dbtest2.settings")
django.setup()

from draw.draw_home_line import draw_home_line
from draw.draw_home_pie1 import draw_pie1
from draw.draw_home_pie2 import draw_pie2
from draw.draw_home_pie3 import draw_pie3
from draw.draw_home_pie4 import draw_pie4
from draw.draw_home_pie5 import draw_pie5
from draw.draw_home_pie6 import draw_pie6
from draw.draw_home_pie7 import draw_pie7
from draw.draw_home_pie8 import draw_pie8

from draw.draw_bar import draw_bar
from draw.draw_line import draw_line
from draw.draw_pie import draw_pie

def drawAlljs():
    draw_pie1()  # home的扇形图
    draw_pie2()  # home的扇形图
    draw_pie3()  # home的扇形图
    draw_pie4()  # home的扇形图
    draw_pie5()  # home的扇形图
    draw_pie6()  # home的扇形图
    draw_pie7()  # home的扇形图
    draw_pie8()  # home的扇形图
    draw_home_line('/home/yc/PycharmProjects/dbtest2/static/drawjs/homepage_linechart.js')  # home的折线图


    draw_bar('/home/yc/PycharmProjects/dbtest2/static/drawjs/secondpage_barchart.js')    # 第二个页面的开心柱状图
    draw_line('/home/yc/PycharmProjects/dbtest2/static/drawjs/secondpage_linechart.js')  # 第二个页面的开心折线图
    draw_pie('/home/yc/PycharmProjects/dbtest2/static/drawjs/secondpage_piechart.js')    # 第二个页面的开心扇形图图
    return True