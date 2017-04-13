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

# bk = xlrd.open_workbook('D:\ddd.xls')
ak = xlrd.open_workbook('D:\\variant.xls')
ck = xlrd.open_workbook('D:\\exovariant2.xls')
dk = xlrd.open_workbook('D:\end3.xls')
bk = xlrd.open_workbook('D:\\a3.xls')

#get the sheets number
shxrange = range(bk.nsheets)
shxrange1 = range(ak.nsheets)
shxrange2 = range(ck.nsheets)
shxrange3 = range(dk.nsheets)



sh = bk.sheets()[0]
ss = ak.sheets()[0]
shuju = ck.sheets()[0]
dkk = dk.sheets()[0]


w = xlutils.copy.copy(ak)
w1 = xlutils.copy.copy(ck)
wb = xlutils.copy.copy(bk)
wd = xlutils.copy.copy(dk)

ws = w.get_sheet(0)
wshuju = w1.get_sheet(0)
wbb = wb.get_sheet(0)
wdd = wd.get_sheet(0)

ssnrows = ss.nrows
ssncols = ss.ncols
nrows = sh.nrows
ncols = sh.ncols
shujunrows = shuju.nrows
shujuncols = shuju.ncols
dkknrows = dkk.nrows
dkkncols = dkk.ncols




for i in range(dkknrows):
    ashuju = ''
    bshuju = ''
    bshuju2 = ''
    start = str(dkk.cell_value(i, 1))
    print start
    for j in range(ssnrows):
        cell_valueb = ss.cell_value(j, 3)
        if start in str(cell_valueb):
            bshuju = str(ss.cell_value(j,1))
            print 'bshuju',bshuju
    for l in range(shujunrows):
        cell_valueb2 = shuju.cell_value(l, 4)
        if start in str(cell_valueb2):
            bshuju2 = str(shuju.cell_value(l,2))
            print 'bshuju2',bshuju2
    for k in range(nrows):
        cell_valuea = sh.cell_value(k, 2)
        # print 'aa',cell_valuea
        if start in str(cell_valuea):
            ashuju = str(sh.cell_value(k,21))
            print 'ashuju',ashuju
    if ashuju in bshuju:
        wdd.write(i, 5, ashuju)
        # wdd.write(i, 6, bshuju + ',' + bshuju2)
        wdd.write(i, 7, 'true')
    elif ashuju in bshuju2:
        wdd.write(i, 5, ashuju)
        # wdd.write(i, 6, bshuju + ',' + bshuju2)
        wdd.write(i, 7, 'true')
    else:
        wdd.write(i, 5, ashuju)
        wdd.write(i, 7, 'false')
    if ashuju == '':
        wdd.write(i, 7, 'false')
    elif bshuju =='' and bshuju2 =='':
        wdd.write(i, 7, 'false')
    wdd.write(i, 6, bshuju + ',' + bshuju2)
wd.save('D:\end3.xls')






# for k in range(1, 340):
#     print 'k = ', k
#     ex = hang
#     xx2 = xx1
#     # print ss.cell_value(k, 2)
#     if ss.cell_value(k, 2) == 'NULL' or ss.cell_value(k, 2) == '':
#         pass
#     else:
#         testin1 = str(ss.cell_value(k, 2))
#         print testin1
#         print type(testin1)
#         # words = WordPunctTokenizer().tokenize(testin1)
#         words = re.findall("\\w*?[a-z]\\w*", testin1, re.I)
#         print 'words ', words
#         print type(words)
#
#         # data1 = data1.union(words)
#         # data = list(set(data1))
#         # print 'data1 ', list(data1)
#         # print 'len   ', len(list(data1))
#         for i in range(len(words)):
#             if words[i] not in data1:
#                 data1.append(words[i])
#         # data = list(data1)
#         data = data1
#         print 'data', words
#         print 'data1',list(data1)
# for j in range(len(data)):
#             testin2 = str(data[j])
#             outputdata = []
#             outputs = []
#             for i in range(nrows):
#                 cell_value = sh.cell_value(i, 3)
#                 if testin2 in str(cell_value):
#                     outputs = sh.row_values(i)
#                     outputdata.append(outputs)
#             print 'outputdata', outputdata
#             num = len(outputdata)
#             if outputdata:
#                 print 'j', j
#                 for ii in range(num):
#                     if testin2 == ',':
#                         pass
#                     else:
#                         print 'xx2' ,xx2
#                         if outputdata[ii][3] == 'NA':
#                             pass
#                         else:
#                             wshuju.write(xx2, 0, testin2)
#                             wshuju.write(xx2, 1, str(outputdata[ii][3]))
#                             wshuju.write(xx2, 2, str((outputdata[ii][0])))
#                             xx = xx + 1
#                             xx1 = xx1 + 1
#                             xx2 = xx2 + 1
#
#             else:
#                 pass
#



# w1.save('D:\shuju.xls')
