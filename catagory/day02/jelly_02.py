#!/usr/bin/python
# coding=utf-8

# 类型有五大类:数字,字符串,列表,元组,字典
# 数字有以下子类型: int(有符号整型),long(长整型[也可以代表八进制和十六进制]),float(浮点型),complex(复数)

num = 3
f_num = 3.00
# long 类型只存在于 Python2.X 版本中，在 2.2 以后的版本中，int 类型数据溢出后会自动转为long类型。在 Python3.X 版本中 long 类型被移除，使用 int 替代
l_num = 10L
c_num = 3.14j

print type(num)
print type(f_num)
print type(l_num)
print type(c_num)

# 字符串或串(String)是由数字、字母、下划线组成的一串字符。
sequence = "我是python"
print type(sequence)

# 列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）.列表用 [ ] 标识，是 python 最通用的复合数据类型。
l_list = ["x"]
print type(l_list)
print l_list

# tuple 元组,元组是另一个数据类型，类似于 List（列表）。元组用 () 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
m_meta = ()
print type(m_meta)
print m_meta

# 字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。
# 两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
d_meta = {}
print type(d_meta)
print d_meta

# 数据转换的方式主要为数据类型比如 int() long() float() tuple() dict() str() complex()
n_s_str = '8'
print int(n_s_str)
print type(int(n_s_str))
u_sequence = u"我是python"

print type(u_sequence)


