#!/usr/bin/python
# -*- coding:utf-8 -*-

# @Time :2019-11-12 10:21
# @Author: cd
# @FileName:rule.py
# @Copyright: @2019-2020

# 说下python的规则,首先一个文件就是一个模块,在模块中的方法只能通过模块名称来引用.
___NAME___ = "rule.py"


class rule:

    def __init__(self):
        print "rule init"
        pass

    def po(self):

        print "I'm Rule!!!"


class PRule:

    def __init__(self):
        print "init"
        pass

    def po(self):
        print "PRule print"
