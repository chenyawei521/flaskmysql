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
    # sheet.write(i, 0, x[i].decode('utf-8'))
    sheet.write(i, 0, x[i])
book.save('d:\ fff.xls')
# print len(y2)
# print "y=", y2[0]


# for i in range(len(y2)):
# #    print x[i]
#     sheet.write(i, 0, y2[i].decode('utf-8'))
#     sheet.write(i, 0, y2[i])
# book.save('d:\ fff.xls')
