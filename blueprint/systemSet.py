# encoding: utf-8
from flask import Blueprint,render_template,request,redirect,make_response,session,Flask
import hashlib
from config import connect
from pag import pages

systemSet = Blueprint("systemSet",__name__,template_folder="templates",static_folder = "static")

# 修改通知
@systemSet.route('/addNotice')
def addNotice():
    return render_template('systemSet/setNotice.html')
@systemSet.route('/setNotice',methods=["GET"])
def setNotice():
    content = request.args.get('content')
    userid = session.get("userid")
    db = connect()
    cur = db.cursor()
    cur.execute('insert into notice (content,create_userid) values (%s,%s)', (content,userid))
    db.commit()
    db.close()
    cur.close()
    return "success"
# 管理员工具
@systemSet.route('/tool')
def tool():
    type = request.args.get("type") or "1"
    content = request.args.get("content") or "1"
    type = "1" if content == "1" else type
    db = connect()
    cur = db.cursor()
    cur.execute('select userid from user_info where state = 1 and ' + type + ' = %s', (content))
    pag = pages(len(cur.fetchall()), 10)
    lim = pag['limit']
    cur.execute('select userid,name,role from user_info where state = 1 and ' + type + '= %s' + lim,(content))
    results = cur.fetchall()
    db.commit()
    db.close()
    cur.close()
    for item in results:
        if item["role"] == "admin":
            item["role"] = "管理员"
        elif item["role"] == "teacher":
            item["role"] = "教师"
        elif item["role"] == "student":
            item["role"] = "学生"
    return render_template('systemSet/tool.html', data=results, pag=pag)
# 重置密码
@systemSet.route('/resetPssword/<userid>')
def resetPssword(userid):
    db = connect()
    cur = db.cursor()
    md5 = hashlib.md5()
    md5.update("123456".encode("utf8"))
    password = md5.hexdigest()
    cur.execute("update user_info set password = %s where userid= %s",(password,userid))
    db.commit()
    db.close()
    cur.close()
    return "success"
#冻结用户
@systemSet.route('/deleteUser/<userid>')
def deleteUser(userid):
    db = connect()
    cur = db.cursor()
    cur.execute("select role from user_info where userid = %s",(userid))
    result = cur.fetchone()
    cur.execute("update user_info set state = 0 where userid= %s", (userid))
    if result["role"] == "teacher":
        cur.execute("update teacher_info set state = 0 where userid= %s", (userid))
    elif result["role"] == "student":
        cur.execute("update student_info set state = 0 where userid= %s", (userid))
    db.commit()
    db.close()
    cur.close()
    return "success"
# 专业方向管理
@systemSet.route('/majorSet',methods=["GET"])
def majorSet():
    db = connect()
    cur = db.cursor()
    cur.execute("select major_id from majortable where state = 1")
    pag = pages(len(cur.fetchall()), 10)
    lim = pag['limit']
    cur.execute("select major_id,major_name from majortable where state = 1" + lim)
    results = cur.fetchall()
    db.close()
    cur.close()
    return render_template('systemSet/setMajor.html',data=results, pag=pag)
@systemSet.route('/addMajor',methods=["POST"])
def addMajor():
    major_name = request.form["major_name"] or ""
    if not major_name:
        return render_template("fail.html")
    else:
        db = connect()
        cur = db.cursor()
        cur.execute("select major_id from majortable where major_name = %s",(major_name))
        if cur.fetchone():
            return render_template("fail.html")
        cur.execute("insert into majortable (major_name) values (%s)",(major_name))
        db.commit()
        db.close()
        cur.close()
        return render_template("success.html")
# 修改删除





# 添加单个用户
@systemSet.route('/adduser',methods=["GET"])
def adduser():
    db = connect()
    cur = db.cursor()
    cur.execute("select major_id,major_name from majortable where state = 1")
    results = cur.fetchall()
    db.close()
    cur.close()
    return render_template('systemSet/adduser.html',data=results)
@systemSet.route('/adduser',methods=["POST"])
def addsingleuser():
    userid = request.form["userid"] or ""
    password = request.form["password"] or ""
    name = request.form["name"] or ""
    role = request.form["role"] or ""
    sex = request.form["sex"] or ""
    if userid and password and name and role and sex:
        cls = request.form["cls"] or ""
        major_id = request.form["major_id"] or ""
        subject = request.form["subject"] or ""
    else:
        return render_template('fail.html')
    md5 = hashlib.md5()
    md5.update(password.encode("utf8"))
    password = md5.hexdigest()
    db = connect()
    cur = db.cursor()
    cur.execute("insert into user_info (userid,password,name,role) values(%s,%s,%s,%s)",(userid,password,name,role))
    if role == "student":
        cur.execute("insert into student_info (stu_id,name,sex,cls_id,major_id) values (%s,%s,%s,%s,%s)",(userid,name,sex,cls,major_id))
    elif role == "teacher":
        cur.execute("insert into teacher_info (tea_id,name,sex,subject) values (%s,%s,%s,%s)",(userid, name, sex, subject))
    db.commit()
    db.close()
    cur.close()
# 批量添加用户
@systemSet.route('/addxlsx')
def addxlsx():
    return render_template('systemSet/addusers.html')