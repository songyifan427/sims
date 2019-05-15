# encoding: utf-8
from flask import Blueprint,render_template,request,redirect,make_response,session,Flask
from config import connect
from pag import pages

personal = Blueprint("personal",__name__,template_folder="templates",static_folder = "static")

# 查看个人信息
@personal.route('/info')
def info():
    role = session.get("role")
    db = connect()
    cur = db.cursor()
    if role == "teacher":
        cur.execute('select tea_id,name,sex,project,cls_ids from teacher_info where tea_id=%s', (session.get("userid")))
        result = cur.fetchone()
        result["cls_ids"] = result["cls_ids"][:-1] if result["cls_ids"] else ""
        result["role"] = "教师"
    elif role == "student":
        cur.execute('select stu_id,name,sex,cls_id,major_id from student_info where stu_id=%s',(session.get("userid")))
        result = cur.fetchone()
        cur.execute('select major_name from majortable where id=%s', (result["major_id"]))
        result["major_name"] = cur.fetchone()["major_name"]
        result["role"] = "学生"
    else:
        result = {"userid": session.get("userid"),"role" : "管理员"}
    db.close()
    cur.close()
    return render_template("personal/perInfo.html",data = result)
# 查看学生成绩
@personal.route('/score')
def score():
    pass
# 查看教学评估
@personal.route('/estimate')
def estimate():
    type = request.args.get("type") or "1"
    content = request.args.get("content") or "1"
    type = "1" if content == "1" else type
    db = connect()
    cur = db.cursor()
    cur.execute('select id from estimate where tea_id = %s and state=1 and %s = %s', (session.get("userid"),type,content))
    pag = pages(len(cur.fetchall()), 5)
    lim = pag['limit']
    cur.execute('select content,create_time from estimate where tea_id = %s and state = 1 and %s = %s' + lim, (session.get("userid"),type,content))
    result = cur.fetchall()
    if result:
        for item in result:
            item["create_time"] = item["create_time"].strftime('%Y-%m-%d')
    db.close()
    cur.close()
    return render_template('personal/perEstimate.html', data = result, pag = pag)