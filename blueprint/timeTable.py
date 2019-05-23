# encoding: utf-8
from flask import Blueprint,render_template,request,redirect,make_response,session,Flask
from config import connect
from pag import pages

timeTable = Blueprint("timeTable",__name__,template_folder="templates",static_folder = "static")

# 查看班级课表
@timeTable.route('/seeclass')
def seeclass():
    pass
# 查看我的课表
@timeTable.route('/seeperson')
def seepersonal():
    pass
# 管理课表
@timeTable.route('/manage')
def manage():
    pass
# 新建课表
@timeTable.route('/build')
def build():
    pass