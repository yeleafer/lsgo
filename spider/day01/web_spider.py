#!/usr/bin/python
# -*- coding:utf-8 -*-

# @Time :2019-11-12 09:17
# @Author: cd
# @FileName:web_spider.py
# @Copyright: @2019-2020
# 正则表达式
import re
# http请求包
import requests
# BeautifulSoup包括几部分 BeautifulSoup/BeautifulStoneSoup/BeautifulSOAP
# BeautifulSoup用来解析HTML/BeautifulStoneSoup用来解析XML
from BeautifulSoup import BeautifulSoup
doc = ['<html><head><title>Page title</title></head>',
       '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
       '</html>']
soup = BeautifulSoup(''.join(doc))

print soup.prettify()
# <html>
#  <head>
#   <title>
#    Page title
#   </title>
#  </head>
#  <body>
#   <p id="firstpara" align="center">
#    This is paragraph
#    <b>
#     one
#    </b>
#    .
#   </p>
#   <p id="secondpara" align="blah">
#    This is paragraph
#    <b>
#     two
#    </b>
#    .
#   </p>
#  </body>
# </html>
print soup.contents[0].head.title.string
print soup.contents[0].contents[1].name
# 获取属性,结果是一个元组,元组通过索引获取值
print soup.contents[0].contents[1].contents[1].attrs[0][0]
print soup.contents[0].contents[1].contents[1].attrs[0][1]
# 另外的方式
title_tag = soup.html.head.title

print title_tag.string

