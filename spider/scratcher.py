#!/usr/bin/python
# -*- coding:utf-8 -*-

# @Time :2019-11-06 19:25
# @Author: cd
# @FileName:scratcher.py
# @Copyright: @2019-2020

import requests
url = 'http://www.htouhui.com'

strHtml = requests.get(url)
print strHtml.text
