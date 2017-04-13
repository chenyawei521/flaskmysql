#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re, xlwt
# 打开一个文件
book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('dede', cell_overwrite_ok=True)
sheet.write(0, 0, 'ddddd')
book.save('d:\ fff.xls')
fo = open("aa2.txt", "r+")
str1 = fo.read()
print "读取的字符串是 : ", str1

# str1 = str.decode("gb2312",)

# 关闭打开的文件
fo.close()
# p = ".+\n"
# a = "诊断.+\n"
a = "(?<=qq)[\s\S]*?(?=qw)"
# a = "诊断\:.+\n"
b = re.compile(u"[\u4e00-\u9fa5]{1,2}")
pa = re.compile(a)
print pa.findall(str1)
x = pa.findall(str1)
print len(x)
# y1 = str(x)
# c = "许多.+\n"
# d = re.compile(c)
# y2 = d.findall(x[0])

# print "y=", y
for i in range(len(x)):
    print x[i]
    name = "(?<=kk)[\s\S]*?(?=\n)"
    name1 = re.compile(name)
    namestr = name1.findall(x[i])
    # print type(namestr)
    # print len(namestr)
    # print namestr[0]
    # sheet.write(i, 0, x[i].decode('utf-8'))
    if namestr:
        sheet.write(i, 0, namestr[0])
    # zhen = "(?<=诊断)[\s\S]*?(?=\n)"

    zhi = "(治疗\:.+\n)"
    zhi1 = re.compile(zhi)
    zhistr = zhi1.findall(x[i])
    if zhistr:
        sheet.write(i, 1, zhistr[0])

    jian = "(建议\:.+\n)"
    jian1 = re.compile(jian)
    jianstr = jian1.findall(x[i])
    if jianstr:
        sheet.write(i, 2, jianstr[0])

    que = "(确诊\:.+\n)"
    que1 = re.compile(que)
    questr = que1.findall(x[i])
    if questr:
        sheet.write(i, 3, questr[0])

    zhen = "(诊断\:.+\n)"
    zhen1 = re.compile(zhen)
    zhenstr = zhen1.findall(x[i])
    if zhenstr:
        sheet.write(i, 4, zhenstr[0])

    biao = "(表现\:.+\n)"
    biao1 = re.compile(biao)
    biaostr = biao1.findall(x[i])
    if biaostr:
        sheet.write(i, 5, biaostr[0])

    fa = "(发病率\:.+\n)"
    fa1 = re.compile(fa)
    fastr = fa1.findall(x[i])
    if fastr:
        sheet.write(i, 6, fastr[0])

    sheng = "(生化\:.+\n)"
    sheng1 = re.compile(sheng)
    shengstr = sheng1.findall(x[i])
    if shengstr:
        sheet.write(i, 7, shengstr[0])

    bing = "(并发症\:.+\n)"
    bing1 = re.compile(bing)
    bingstr = bing1.findall(x[i])
    if bingstr:
        sheet.write(i, 8, bingstr[0])

    yu = "(预后\:.+\n)"
    yu1 = re.compile(yu)
    yustr = yu1.findall(x[i])
    if yustr:
        sheet.write(i, 9, yustr[0])

    mei = "(酶学\:.+\n)"
    mei1 = re.compile(mei)
    meistr = mei1.findall(x[i])
    if meistr:
        sheet.write(i, 10, meistr[0])

    qi = "(起病\:.+\n)"
    qi1 = re.compile(qi)
    qistr = qi1.findall(x[i])
    if qistr:
        sheet.write(i, 11, qistr[0])

    fab = "(发病\:.+\n)"
    fab1 = re.compile(fab)
    fabstr = fab1.findall(x[i])
    if fabstr:
        sheet.write(i, 12, fabstr[0])

    meiq = "(酶缺陷\:.+\n)"
    meiq1 = re.compile(meiq)
    meiqstr = meiq1.findall(x[i])
    if meiqstr:
        sheet.write(i, 13, meiqstr[0])

    jianb = "(鉴别诊断\:.+\n)"
    jianb1 = re.compile(jianb)
    jianbstr = jianb1.findall(x[i])
    if jianbstr:
        sheet.write(i, 14, jianbstr[0])
book.save('d:\ fff.xls')
# print len(y2)
# print "y=", y2[0]


# for i in range(len(y2)):
# #    print x[i]
#     sheet.write(i, 0, y2[i].decode('utf-8'))
#     sheet.write(i, 0, y2[i])
# book.save('d:\ fff.xls')
