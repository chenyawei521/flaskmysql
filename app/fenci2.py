# -*- coding: UTF-8 -*-
import os
import xlrd,sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')
from xlutils.copy import copy
import xlutils
import json
import nltk
from nltk.tokenize import WordPunctTokenizer

#open the excel file
bk = xlrd.open_workbook('D:\ddd.xls')
ak = xlrd.open_workbook('D:\ss.xls')
ck = xlrd.open_workbook('D:\shuju.xls')
#get the sheets number
shxrange = range(bk.nsheets)
shxrange1 = range(ak.nsheets)
shxrange2 = range(ck.nsheets)

# #get the sheets name
# for x in shxrange:
#     p = bk.sheets()[x].name.encode('utf-8')
#     print "Sheets Number(%s): %s" % (x, p.decode('utf-8'))
# #get the sheets name
# for x1 in shxrange1:
#     q = ak.sheets()[x].name.encode('utf-8')
#     print "Sheets Number(%s): %s" % (x1, q.decode('utf-8'))
# # input your sheets name
# # sname=int(raw_input('choose the sheet number:'))
try:
    sh = bk.sheets()[0]
except:
    print "no this sheet"
#return None
ss = ak.sheets()[0]
shuju = ck.sheets()[0]
w = xlutils.copy.copy(ak)
w1 = xlutils.copy.copy(ck)
ws = w.get_sheet(0)
wshuju = w1.get_sheet(0)
ssnrows = ss.nrows
ssncols = ss.ncols
nrows = sh.nrows
ncols = sh.ncols
shujunrows = shuju.nrows
shujuncols = shuju.ncols
hang = 0
ex = 0
xx = 0
xx1 = 0
xx2 = 0
data1 = []
data2 = []
data = []
for k in range(1, 340):
    print 'k = ', k
    ex = hang
    xx2 = xx1
    # print ss.cell_value(k, 2)
    if ss.cell_value(k, 2) == 'NULL' or ss.cell_value(k, 2) == '':
        pass
    else:
        testin1 = str(ss.cell_value(k, 2))
        print testin1
        print type(testin1)
        # words = WordPunctTokenizer().tokenize(testin1)
        words = re.findall("\\w*?[a-z]\\w*", testin1, re.I)
        print 'words ', words
        print type(words)

        # data1 = data1.union(words)
        # data = list(set(data1))
        # print 'data1 ', list(data1)
        # print 'len   ', len(list(data1))
        for i in range(len(words)):
            if words[i] not in data1:
                data1.append(words[i])
        # data = list(data1)
        data = data1
        print 'data', words
        print 'data1',list(data1)
for j in range(len(data)):
            testin2 = str(data[j])
            outputdata = []
            outputs = []
            for i in range(nrows):
                cell_value = sh.cell_value(i, 3)
                if testin2 in str(cell_value):
                    outputs = sh.row_values(i)
                    outputdata.append(outputs)
            print 'outputdata', outputdata
            num = len(outputdata)
            if outputdata:
                print 'j', j
                for ii in range(num):
                    if testin2 == ',':
                        pass
                    else:
                        print 'xx2' ,xx2
                        if outputdata[ii][3] == 'NA':
                            pass
                        else:
                            wshuju.write(xx2, 0, testin2)
                            wshuju.write(xx2, 1, str(outputdata[ii][3]))
                            wshuju.write(xx2, 2, str((outputdata[ii][0])))
                            xx = xx + 1
                            xx1 = xx1 + 1
                            xx2 = xx2 + 1

            else:
                pass




w1.save('D:\shuju.xls')
