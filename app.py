# encoding: utf-8
from flask import Flask,render_template,request,redirect,make_response,session,url_for
import hashlib
from code import code
from config import secret_key,maxcontent,connect

# 蓝图
from blueprint.personal import personal
# from blueprint.timeTable import timeTable
# from blueprint.infoSet import infoSet
# from blueprint.score import score
# from blueprint.estimate import estimate
# from blueprint.systemSet import systemSet

app = Flask(__name__,template_folder="templates",static_folder = "static")
app.secret_key=secret_key
app.config['MAX_CONTENT_LENGTH'] = maxcontent

app.register_blueprint(personal,url_prefix="/personal")
# app.register_blueprint(timeTable,url_prefix="/timeTable")
# app.register_blueprint(infoSet,url_prefix="/infoSet")
# app.register_blueprint(score,url_prefix="/score")
# app.register_blueprint(estimate,url_prefix="/estimate")
# app.register_blueprint(systemSet,url_prefix="/systemSet")

# 错误
# @app.route('/404')
# def e404():
#     return render_template('404.html')
# @app.errorhandler(404)
# def error(error):
#     # return redirect(url_for('.e404'))
#     return render_template('404.html')
# 操作成功和失败
@app.route('/success')
def success():
    return render_template('success.html')
@app.route('/fail')
def fail():
    return render_template('fail.html')

# 访问根目录
@app.route('/')
def index():
    if(session.get("login")=="yes"):
        db = connect()
        cur = db.cursor()
        cur.execute('select content,create_time from notice order by id desc limit 1')
        result = cur.fetchone()
        if (result):
            notice = result["content"]
            day = result["create_time"].strftime('%Y-%m-%d')
        else:
            notice = ""
            day = "无通知"
        db.commit()
        db.close()
        cur.close()
        res=make_response(render_template('index.html',data={'name':session.get('name'),'notice':notice,'day':day},role=session.get('role')))
        return res
    else:
        return  redirect('/login')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/codeimg')
def codeimg():
    codeobj=code()
    res=make_response(codeobj.output())
    session["code"]=codeobj.str.lower()
    res.headers["content-type"]="image/png"
    return res
# 验证登录
@app.route('/checklogin',methods=["POST"])
def checklogin():
    if (session.get("code") == request.form["code"].lower()):
        db = connect()
        cur = db.cursor()
        userid=request.form["userid"]
        password=request.form["password"]
        md5=hashlib.md5()
        md5.update(password.encode("utf8"))
        upass=md5.hexdigest()
        cur.execute('select role from user_info where userid=%s and password=%s',(userid,upass))
        result=cur.fetchone()
        if(result):
            res = make_response(redirect('/'))
            session["login"]="yes"
            session["userid"]=userid
            session["role"]=result["role"]
            if result["role"]=="student":
                cur.execute('select name from student_info where stu_id=%s', (userid))
                session["name"] = cur.fetchone()["name"]
            elif result["role"]=="teacher":
                cur.execute('select name from teacher_info where tea_id=%s', (userid))
                session["name"] = cur.fetchone()["name"]
            else:
                session["name"]="管理员"
            db.close()
            cur.close()
            session.pop("code")
            return res
        else:
            db.close()
            cur.close()
            return render_template('login.html',tips="用户名或密码不正确")
    else:
        return render_template('login.html',tips="验证码不正确")
# 消息历史
@app.route('/message')
def message():
    db = connect()
    cur = db.cursor()
    cur.execute("select content,create_time from notice order by id desc")
    result = cur.fetchall()
    for item in result:
        item["create_time"] = item["create_time"].strftime('%Y-%m-%d')
    return render_template('message.html', notices=result)
# 退出登录
@app.route('/logout')
def logout():
    res = make_response(redirect('/'))
    session.pop("login")
    session.pop("userid")
    session.pop("name")
    session.pop("role")
    return res
# 修改密码
@app.route('/myinfo')
def myinfo():
    return render_template('setPassword.html')
@app.route('/setPassword',methods=["POST"])
def setPassword():
    password = request.form["password"]
    md5 = hashlib.md5()
    md5.update(password.encode("utf8"))
    password = md5.hexdigest()
    userid=session.get('userid')
    db = connect()
    cur = db.cursor()
    cur.execute('select userid from user_info where userid=%s and password=%s', (userid, password))
    result = cur.fetchone()
    if(result):
        newpassword1 = request.form["inputPassword1"]
        newpassword2 = request.form["inputPassword2"]
        if newpassword1==newpassword2:
            md5 = hashlib.md5()
            md5.update(newpassword2.encode("utf8"))
            newpassword = md5.hexdigest()
            cur.execute('update user_info set password=%s where userid=%s', (newpassword, userid))
            db.commit()
            db.close()
            cur.close()
            return render_template('success.html')
        else:
            db.close()
            cur.close()
            return render_template('fail.html')
    else:
        db.close()
        cur.close()
        return render_template('fail.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)

