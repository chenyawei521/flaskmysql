# -*- coding: UTF-8 -*-
import os
import xlrd,sys
reload(sys)
sys.setdefaultencoding('utf-8')
from xlutils.copy import copy
import xlutils
import re
import json
import nltk
from nltk.tokenize import WordPunctTokenizer

#open the excel file
bk = xlrd.open_workbook('D:\ddd.xls')
ak = xlrd.open_workbook('D:\ss.xls')
ck = xlrd.open_workbook('D:\shuju2.xls')
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
desease = []
desease1= []
for kk in range(1,340):
    desease.append(ss.cell_value(kk, 2))
print 'desease' ,desease
for i in range(len(desease)):
    if desease[i] not in desease1:
        desease1.append(desease[i])
print  'desease1' ,desease1
print  'len desease1' ,len(desease1)
print  'len desease' ,len(desease)
for k in range(len(desease1)):
    print 'k = ', k
    ex = hang
    xx2 = xx1
    # print ss.cell_value(k, 2)
    if desease1[k]== 'NULL' or desease1[k] == '':
        pass
    else:
        words = re.findall("\\w*?\w{3,50}\\w*", desease1[k], re.I)
        print words
        print type(words)

        for j in range(len(words)):
            testin2 = words[j]
            outputdata = []
            outputs = []
            geneid = ''
            xx1 = xx
            for i in range(nrows):
                cell_value = sh.cell_value(i, 3)
                if testin2 in str(cell_value):
                    outputs = sh.row_values(i)
                    outputdata.append(outputs)
            print 'outputdata', outputdata
            print type(outputdata)
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
                            wshuju.write(xx2, 0, desease1[k])
                            wshuju.write(xx2, 1, str(outputdata[ii][0]))
                            wshuju.write(xx2, 2, str(outputdata[ii][3]))
                            wshuju.write(xx2, 3, testin2)
                            xx = xx + 1
                            xx1 = xx1 + 1
                            xx2 = xx2 + 1
                        # geneid = geneid + '  ' + str(int(outputdata[ii][0]))
                    # print hang
                    # wshuju.write(ex, 0, testin2)
                    # wshuju.write(ex, 1, geneid)
                    # print 'ex', ex
                    # hang = hang + 1
                    # ex = ex + 1
            else:
                pass

            # num = len(outputdata)
            # if outputdata == 0:
            #     pass
            # else:
            #     geneid = ''
            #     genename = ''
            #     phenoid = ''
            #     phenoname = ''
            #     Inheritance = ''
            #     for ii in range(num):
            #         geneid = geneid + '  ' + str(int(outputdata[ii][0]))
            #         genename = genename + '  ' + str(outputdata[ii][5])
            #         phenoid = phenoid + '  ' + str(outputdata[ii][2])
            #         phenoname = phenoname + '  ' + str(outputdata[ii][3])
            #         Inheritance = Inheritance + '  ' + str(outputdata[ii][4])
            # print 'json data is', json.dumps(outputs)
            # wshuju.write(j, 13, geneid)
            # wshuju.write(j, 12, phenoname)
            # wshuju.write(j, 11, phenoid)
            # wshuju.write(j, 14, genename)
            # wshuju.write(j, 15, json.dumps(outputs))
        w1.save('D:\shuju2.xls')
