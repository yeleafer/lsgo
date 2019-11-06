#!usr/bin/python
# coding=utf-8

# 条件呢语句 if
if True:
    print "条件通过"
else:
    print "条件未通过"

if False:
    print "条件未通过"
else:
    print "条件通过"

# 多条件
if False:
    print "False"
elif True:
    print "True"
else:
    print "OTHER"

# Python 编程中 while 语句用于循环执行程序，即在某条件下，循环执行某段程序，以处理需要重复处理的相同任务。其基本形式为：
# 循环,python是没有 ++和--操作的,原因就在于python模型规定 数值对象值不能被改变
x = 1
while True:
    x = x+1
    if x > 10:
        print x
        break
# python的for循环的功能变得单一,即遍历list元素,而不像其他语言一样包含条件判断 主要形式就是 for in,for item in (字符串,列表)
# Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串
num_list = [1, 2, 3, 4, 5]
for num in num_list:
    num += 1
    print num
