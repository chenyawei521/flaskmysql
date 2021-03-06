# -*- coding: UTF-8 -*-
from flask import Flask, session, url_for, request, render_template, redirect, g
import MySQLdb
import logging
import traceback
app = Flask(__name__)
app.secret_key = '\xf1\x92Y\xdf\x8ejY\x04\x96\xb4V\x88\xfb\xfc\xb5\x18F\xa3\xee\xb9\xb9t\x01\xf0\x96'
# 配置secret_key,否则不能实现session对话



conn2 = MySQLdb.connect('localhost', 'root', '123456', 'new')
cur2 = conn2.cursor()
# cur2.execute("drop table table3")
# cur2.execute("create table table3(name char(10),password char(10))")
# cur2.execute("insert into table3 values( 'chen','123456'),('chang','123456'),('zhen','123456')")
# cur2.execute('SELECT * FROM table3;')
# result1 = cur2.fetchall()
# '''cur2.execute("select count(*) from table1 where name='chen'and password ='123456'")
# result=cur2.fetchall()'''
# print result1

@app.before_request
def before_request():
    try:
        fh = open("testfile", "r")
        fh.write("测试")
    except IOError, msg:
        exstr = traceback.format_exc()
        print 'exstr', exstr
        print type(exstr)
        logging.exception(exstr)
        print 'msg', msg
    else:
        print "写入成功"
        fh.close()
@app.before_request
def before_request():
    print 'rrr'
    # print type(g)
@app.before_request
def before_request():
    print 'yyy'


@app.before_request
def before_request():

    # cur2.execute('drop table table3')
    # cur2.execute("create table table3(name char(10),password char(10))")
    # cur2.execute("create table table1(name char(10),password char(10))")
    cur2.execute("insert into table1 values( 'chen','123456'),('chang','123456'),('zheng','123456')")
    # cur2.execute('SELECT * FROM table1;')
    # result1 = cur2.fetchall()
    '''cur2.execute("select count(*) from table1 where name='chen'and password ='123456'")
    result=cur2.fetchall()'''
#     print 'result1', result1


@app.route("/hello")
def hello():
    return 'hello'


@app.route("/hi")
def hi():
    return 'hi'


@app.route("/")
def index():
    x = session.get('username')
    y = session.get('password')
    print x, y
    cur2.execute("select * from table1 where name= '"+str(x)+"'and password = '"+str(y)+"'")
    result2 = cur2.fetchall()
    print result2, type(result2)
    if type(result2) == tuple and result2 == ():
        return redirect(url_for('login'))
    else:
        return 'welcome'
    # list_name = [x,y]
    # print list_name
    # print result2

    '''if session.get('username') == 'shiyanlou' and session.get('password') == 'shiyanlou':
        return "hello shiyanlou"
    else :return "you are not logged in"'''
    '''for i in range(len(result1)):
        for j in range(len(result1[i])):
            if session.get('username') == result1[i][j] and session.get('password') == result1[i][j+1]:
                return "hello welcome"
            #else: return "you are not logged in"
            else:return redirect(url_for('login'))
    x = session.get('username')
    y = session.get('password')
    cur2.excute("insert into table2 values(x,y)")

    cur2.excute('select name,password from table1 where exists(select *from table2 where table1.name=table2.name)')
    print '''


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        return redirect(url_for('index'))
    return render_template('index.html', title='sign in')


@app.route("/logout")
def logout():
    session.pop('username', None)
    session.pop('password', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
