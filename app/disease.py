# -*- coding: UTF-8 -*-
import os
import xlrd,sys
reload(sys)
sys.setdefaultencoding('utf-8')
from xlutils.copy import copy
import xlutils
import json
import nltk


# input the excel file
# Filename=raw_input('fff.xls')
# if not os.path.isfile(Filename):
#     raise NameError,"%s is not a valid filename"%Filename

#open the excel file
bk = xlrd.open_workbook('D:\ddd.xls')
ak = xlrd.open_workbook('D:\ss.xls')
#get the sheets number
shxrange = range(bk.nsheets)
shxrange1 = range(ak.nsheets)
print shxrange

#get the sheets name
for x in shxrange:
    p = bk.sheets()[x].name.encode('utf-8')
    print "Sheets Number(%s): %s" % (x, p.decode('utf-8'))
#get the sheets name
for x1 in shxrange1:
    q = ak.sheets()[x].name.encode('utf-8')
    print "Sheets Number(%s): %s" % (x1, q.decode('utf-8'))
# input your sheets name
# sname=int(raw_input('choose the sheet number:'))
try:
    sh = bk.sheets()[0]
except:
    print "no this sheet"
#return None
ss = ak.sheets()[0]
w = xlutils.copy.copy(ak)
ws = w.get_sheet(0)

ssnrows = ss.nrows
ssncols = ss.ncols
nrows = sh.nrows
ncols = sh.ncols
# return the lines and col number
# print "line:%d  col:%d" %(nrows,ncols)

# print type(ss.cell_value(1, 18))
#www.iplaypy.com
#input the check column
# columnnum=int(raw_input('which column you want to check pls input the num(the first colnumn num is 0):'))
# while columnnum+1>ncols:
#     columnnum=int(raw_input('your num is out of range,pls input again:'))
# input the searching string and column
# testin=raw_input('input the string:')
for k in range(1, 2):
    print ss.cell_value(k, 2)
    if ss.cell_value(k, 2) == 'NULL' or ss.cell_value(k, 2) == '':
        pass
    else:
        testin1 = str(ss.cell_value(k, 2))
        print testin1
        outputdata = []
        outputs = []
        #find the rows which you want to select and write to a txt file
        for i in range(nrows):
            # cell_value = sh.cell_value(i, columnnum)
            cell_value = sh.cell_value(i, 3)
            if testin1 in str(cell_value):
                outputs = sh.row_values(i)
                outputdata.append(outputs)
        print 'outputdata', outputdata
        # ws.write(0,0,outputs[0])
        # print str(outputdata[0][0])+str(outputdata[1][0])
        num = len(outputdata)
        if outputdata == 0:
            pass
        else:
            geneid = ''
            genename = ''
            phenoid = ''
            phenoname = ''
            Inheritance = ''
            for ii in range(num):
                geneid = geneid + '  ' + str(int(outputdata[ii][0]))
                genename = genename + '  ' + str(outputdata[ii][5])
                phenoid = phenoid + '  ' + str(outputdata[ii][2])
                phenoname = phenoname + '  ' + str(outputdata[ii][3])
                Inheritance = Inheritance + '  ' + str(outputdata[ii][4])
        print 'json data is', json.dumps(outputs)
        ws.write(k, 5, geneid)
        ws.write(k, 4, phenoname)
        ws.write(k, 3, phenoid)
        ws.write(k, 6, genename)
        ws.write(k, 7, json.dumps(outputs))
        w.save('D:\ss.xls')
