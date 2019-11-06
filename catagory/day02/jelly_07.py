#!/usr/bin/python
# -*- coding:utf-8 -*-

# @Time :2019-11-06 15:45
# @Author: cd
# @FileName:jelly_07.py
# @Copyright: @2019-2020


class Cd:
    name = ''

    def __init__(self,name):
        self.name = name
        print "Cd 初始化..."

    def print_name(self, suffix):
        print self.name+suffix


cd = Cd("cd")

cd.print_name("_____")
