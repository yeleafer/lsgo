#!/usr/bin/python
# -*- coding:utf-8 -*-

# @Time :2019-11-12 15:02
# @Author: cd
# @FileName:auto_login.py
# @Copyright: @2019-2020

# 导入selenium2中的webdriver库
from selenium import webdriver
# 加载浏览器配置
# option = webdriver.ChromeOptions()
# option.add_argument("--start-maximized")
# 浏览器不显示受自动测试软件控制
# option.add_argument('disable-infobars')
# 启动时自动全屏（相当于在浏览器界面按F11按键）
# option.add_argument('-kiosk')
# 实例化出一个Firefox浏览器
# driver = webdriver.Chrome(chrome_options=option)
# 页面最大化
# 页面最大化的另一种方法 option.addArguments("--start-maximized");
driver = webdriver.Chrome()

# 设置浏览器窗口的位置和大小
driver.maximize_window()
# driver.set_window_position(20, 40)
# driver.set_window_size(1100, 700)

# 打开一个页面（QQ空间登录页）
driver.get("http://localhost:8081/user/login")

# 登录表单在页面的框架中中，所以要切换到该框架
# driver.switch_to_frame('el-form')

# 通过使用选择器选择到表单元素进行模拟输入和点击按钮提交
driver.find_element_by_name('j_username').clear()
driver.find_element_by_name('j_username').send_keys('admin')
driver.find_element_by_css_selector('input[type="password"]').clear()
driver.find_element_by_css_selector('input[type="password"]').send_keys('admin')#password
driver.find_element_by_class_name('el-button').click()

# do something 跳转到项目列表
driver.get("http://localhost:8081/project/list")
# 退出窗口
#driver.quit()


