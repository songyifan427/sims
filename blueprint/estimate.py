# encoding: utf-8
from flask import Blueprint,render_template,request,session
from config import connect
from pag import pages

estimate = Blueprint("estimate",__name__,template_folder="templates",static_folder = "static")

# 教学评估
@estimate.route('/goestimate')
def goestimate():
    pass
# 开关教学评估
@estimate.route('/switch')
def switch():
    pass