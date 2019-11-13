#!/usr/bin/python
# -*- coding:utf-8 -*-

# @Time :2019-11-12 15:56
# @Author: cd
# @FileName:__init__.py
# @Copyright: @2019-2020

import random


def gbk2312():
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xfe)
    val = u'{head:x}{body:x}'
    str = bytes.fromhex(val).decode('gb2312')

    return str