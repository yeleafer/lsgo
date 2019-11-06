#! /usr/bin/python
# coding=utf-8
import cmath

print dir(cmath)
print cmath.__name__
print cmath.__doc__
print cmath.__file__
print cmath.__package__
print cmath.pi
print cmath.e

# 字符串操作
# + 字符串连接 * 重复输出字符串 []通过索引获取字符串中字符 [:]截取字符串中的一部分数据 in 成员运算符,如果字符串中包含给定的字符则返回True ,not in 和in运算相反
# r/R 原始字符串 -所有的字符串都按照字面的意思来使用,没有转义特殊或不能打印的字符.
# %格式字符串
x = u"我是"
print x+u"谁"

x = u"我是你的"
print x[1]+u"谁"
print x[1:3]+u"谁"

print u"谁" in x
print u"谁" not in x
print u"我" in x
print u"我" not in x
for item in x:
    print item


print "\n"
print r"\n"



