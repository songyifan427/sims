# encoding: utf-8
import pymysql
#本机字体样式ttf文件相对路径
ttfurl = '.\static\Arvo-Regular.ttf'
#session_key
secret_key = '123456'
#最大上传文件大小
maxcontent = 16 * 1024 * 1024
#mysql_host
mysqlhost = "localhost"
#mysql_port
mysqlport = 3306
#mysql_user
user = 'root'
#mysql_password
password = '123456'
#mysql_db
dbname = 'sims'
#连接数据库
def connect():
    return pymysql.connect(host=mysqlhost , port=mysqlport , user=user , passwd=password, db=dbname, charset='utf8',cursorclass=pymysql.cursors.DictCursor)