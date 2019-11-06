# /usr/bin/python
# -*- coding:utf-8 -*-
import time
import calendar

# 元组 无关闭分隔符
x, y = 1, 2
print x
print y

print time.localtime()
print time.time()
print time.gmtime()

# 格式化时间
print time.asctime(time.localtime(time.time()))
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# 字符串转时间
a = "2019-11-06 15:33:10"
print time.mktime(time.strptime(a, "%Y-%m-%d %H:%M:%S"))

# 获取某月日历
cal = calendar.month(2019, 11)
print "以下输出2019年11月份的日历"
print cal

print calendar.isleap(2020)
print calendar.isleap(2019)
