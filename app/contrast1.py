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
dk = xlrd.open_workbook('D:\end2.xls')
bk = xlrd.open_workbook('D:\\a2.xls')

#get the sheets number
shxrange = range(bk.nsheets)
shxrange1 = range(ak.nsheets)
shxrange2 = range(ck.nsheets)
shxrange3 = range(dk.nsheets)



sh = bk.sheets()[0]

#return None
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
wd.save('D:\end2.xls')
