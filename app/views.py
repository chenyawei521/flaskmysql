# -*- coding: UTF-8 -*-
from flask import Flask, session, url_for, request, render_template, redirect
import MySQLdb
app = Flask(__name__)
app.secret_key = '\xf1\x92Y\xdf\x8ejY\x04\x96\xb4V\x88\xfb\xfc\xb5\x18F\xa3\xee\xb9\xb9t\x01\xf0\x96'    #配置secret_key,否则不能实现session对话

conn2 = MySQLdb.connect('localhost', 'root', '123456', 'new')
cur2 = conn2.cursor()
# cur2.execute("create table table3(name char(10),password char(10))")
cur2.execute("insert into table3 values( 'chen','123456'),('chang','123456'),('zhang','123456')")
cur2.execute('SELECT * FROM table3;')
result1 = cur2.fetchall()
'''cur2.execute("select count(*) from table1 where name='chen'and password ='123456'")
result=cur2.fetchall()'''
print result1

@app.route("/")
def index():
    x = session.get('username')
    y = session.get('password')
    print x, y
    # cur2.execute("select count(*) from table1 where name='"+str(x)+"' and password = '"+str(y)+"'")
    # cur2.execute("select count(*) from table1 where name='jjj' and password = '1111'")
    cur2.execute("select * from table1 where name= '"+str(x)+"'")
    result2 = cur2.fetchall()
    print result2, type(result2)
    if type(result2) == tuple and result2 == ():
        return redirect(url_for('login'))
    else:
        return 'hahhah'
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

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        return redirect(url_for('index'))
    return render_template('index.html',
        title = 'hah')


@app.route("/logout")
def logout():
    session.pop('username', None)
    session.pop('password', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
