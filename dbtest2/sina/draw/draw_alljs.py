# coding=utf-8
__author__ = 'gu'


from draw_keywordspage import *
from draw_eventspage import *

from draw_homepage_pie1 import *
from draw_homepage_pie2 import *
from draw_homepage_pie3 import *
from draw_homepage_pie4 import *
from draw_homepage_pie5 import *
from draw_homepage_pie6 import *
from draw_homepage_pie7 import *
from draw_homepage_pie8 import *
from draw_homepage_line import *

from draw_chartspage_line import *
from draw_chartspage_bar import *
from draw_chartspage_pie import *



def draw_base_dir():
    base_dir = '/home/yc/PycharmProjects/dbtest2'
    return base_dir


def draw_all():
    draw_homepage_pie1(draw_base_dir() + '/static/drawjs/homepage_pie1.js')  # home的扇形图
    draw_homepage_pie2(draw_base_dir() + '/static/drawjs/homepage_pie2.js')  # home的扇形图
    draw_homepage_pie3(draw_base_dir() + '/static/drawjs/homepage_pie3.js')  # home的扇形图
    draw_homepage_pie4(draw_base_dir() + '/static/drawjs/homepage_pie4.js')  # home的扇形图
    draw_homepage_pie5(draw_base_dir() + '/static/drawjs/homepage_pie5.js')  # home的扇形图
    draw_homepage_pie6(draw_base_dir() + '/static/drawjs/homepage_pie6.js')  # home的扇形图
    draw_homepage_pie7(draw_base_dir() + '/static/drawjs/homepage_pie7.js')  # home的扇形图
    draw_homepage_pie8(draw_base_dir() + '/static/drawjs/homepage_pie8.js')  # home的扇形图
    draw_homepage_line(draw_base_dir() + '/static/drawjs/homepage_linechart.js')  # home的折线图

    draw_chartspage_bar(draw_base_dir() + '/static/drawjs/chartspage_barchart.js')  # 第二个页面的开心柱状图
    draw_chartspage_line(draw_base_dir() + '/static/drawjs/chartspage_linechart.js')  # 第二个页面的开心折线图
    draw_chartspage_pie(draw_base_dir() + '/static/drawjs/chartspage_piechart.js')  # 第二个页面的开心扇形图图

    draw_keywords(draw_base_dir() + '/templates/keywordspage.html')
    draw_eventspage(draw_base_dir() + '/templates/eventspage.html')

if __name__ == "__main__":
    draw_all()