# -*- coding: UTF-8 -*-
from flask import Flask
import requests
import traceback
import json
app = Flask(__name__)
# @app.before_request
# def before_request():
try:
    fh = open("testfile", "r")
    fh.write("测试")
except IOError, msg:
    exstr = traceback.format_exc()
    print 'exstr', exstr
    print 'msg', msg
else:
    print "写入成功"
    fh.close()
info = {'Content-Type': 'json', 'title': 'except', 'performance': 'xianxiang',
        'occur_time': '2017-3-24', 'remark': 'remark', 'open_id': 'ochiws9U02pmJ8voUngKStVms0U4'}
r = requests.post('https://gene.ac/wx/template/fault/', data=json.dumps(info), headers={"Content-Type":"application/json"})
# r = requests.post('https://gene.ac/wx/template/fault/', json = info)
print 'r = ', r.content

# if __name__ == "__main__":
#     app.run(debug=True)
