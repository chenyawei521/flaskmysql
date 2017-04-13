#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re, xlwt
book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('dede', cell_overwrite_ok=True)
book.save('d:\ fff.xls')
fo = open("hg19_refGene.txt", "r+")
str1 = fo.read()
# print "读取的字符串是 : ", str1
fo.close()
# a = "(?<=NM_033305)[\s\S]*?(?=\n)"
genestr = "NM_014249"
a = "(?<="+genestr+")[\s\S]*?(?=\n)"
pa = re.compile(a)
print pa.findall(str1)
x = pa.findall(str1)

name = "(?<=\s)[\s\S]*?(?=\s)"
name1 = re.compile(name)
namestr = name1.findall(x[0])
print "数据1:", namestr

cdstart1 = int(namestr[4])
cdsend = int(namestr[5])
polar = namestr[1]
extronnum = int(namestr[6])

num = "(\d+)"
num1 = re.compile(num)
numstr = num1.findall(namestr[7])
endnum = "(\d+)"
endnum1 = re.compile(endnum)
endnumstr = endnum1.findall(namestr[8])
print "数据2:", numstr
print len(numstr)
for i in range(len(numstr)):
    # print numstr[i]
    sheet.write(i+1, 0, numstr[i])
    sheet.write(i+1, 1, endnumstr[i])
book.save('d:\ fff.xls')
print type(numstr)


def nearest(locus, cdstart, nums):
# def nearest(locus, nums ):
    dises = []
    min = 1000000000000
    for i in range(len(nums)):
        dis = locus - int(nums[i])
        dises.append(dis)
        if abs(dis) < abs(min):
            min = dis
    idx = dises.index(min) + 1
    ref = int(nums[idx-1]) - cdstart
    dis = min
    return ref, dis, idx
    # return  dis, idx


def err(locus, startnum, endnum):

    intron = 0
    # data = nearest(locus, cdstart1, endnumstr)
    start_near = nearest(locus, cdstart1, numstr)
    end_near = nearest(locus, cdstart1, endnumstr)
    if abs(start_near[1]) > abs(end_near[1]):
        data = end_near
    else:
        data = start_near
    print locus
    print numstr[data[2]-1]
    print endnumstr[data[2]-1]
    totalintron = 0
    pianyi = 0
    for k in range(extronnum-1):
        # print int(startnum[k+1])-int(endnum[k])
        totalintron = totalintron + int(startnum[k+1])-int(endnum[k])
        # print int(startnum[k+1]),int(endnum[k])
        # print int(startnum[j+1])-int(endnum[j])
    totalextron = cdsend - cdstart1 - totalintron
    print "extron", totalextron
    error = 0
    print 'data2', data[2]
    if polar == '+':
        print
        if (locus >= int(numstr[data[2]-1]) and locus <= int(endnumstr[data[2]-1])):
            pianyi = 0
            print '>>><<<<'
            for j in range(int(data[2] - 1)):
                intron = intron + int(startnum[j+1])-int(endnum[j])
                # print int(startnum[j+1])-int(endnum[j])
            error = locus - cdstart1 - intron
        elif locus > int(endnumstr[data[2]-1]):
            print '>>>>'
            pianyi =data[1]
            for j in range(int(data[2] - 1)):
                intron = intron + int(startnum[j+1])-int(endnum[j])
                # print int(startnum[j+1])-int(endnum[j])
            error = data[0] - intron
        elif locus < int(numstr[data[2]-1]):
            pianyi =data[1]
            for j in range(int(data[2] - 1)):
                intron = intron + int(startnum[j+1])-int(endnum[j])
                # print int(startnum[j+1])-int(endnum[j])
            error = data[0] - intron
    else:
        if (locus >= int(numstr[data[2]-1]) and locus <= int(endnumstr[data[2]-1])):
            pianyi = 0
            for j in range(int(data[2] - 1)):
                intron = intron + int(startnum[j+1])-int(endnum[j])
            error = totalextron - (locus - cdstart1 - intron)
        elif locus > int(endnumstr[data[2]-1]):
            pianyi =data[1]
            for j in range(int(data[2] - 1)):
                intron = intron + int(startnum[j+1])-int(endnum[j])
                # print int(startnum[j+1])-int(endnum[j])
            error = totalextron-(data[0] - intron)
        elif locus < int(numstr[data[2]-1]):
            pianyi =data[1]
            for j in range(int(data[2] - 1)):
                intron = intron + int(startnum[j+1])-int(endnum[j])
                # print int(startnum[j+1])-int(endnum[j])
            error = totalextron - (data[0] - intron)
    print data[0]
    print data[1]
    print data[2]
    return error, data[1], data[2], pianyi
# result = nearest(79896780, 79792620, numstr)
# aa = err(79896840, numstr, endnumstr)
# print aa
def gene_locus( locus, numstr, endnumstr):
    err1 = err(locus, numstr, endnumstr)
    print '偏移', err1[3]
    if err1[3] == 0:
        remark = "%s:exon%d:c.%d" % (genestr, err1[2], err1[0])
    else:
        remark = "%s:exon%d:c.%d%+d" % (genestr, err1[2], err1[0], err1[1])
    return remark

remark = gene_locus(8981929, numstr, endnumstr)
print remark
