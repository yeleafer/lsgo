#!/usr/bin/python
# coding=utf-8

# @Time :2019-11-12 15:34
# @Author: cd
# @FileName:gen_project
# @Copyright: @2019-2020

# 自动建标
import time, random
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

# 先登录
driver.get("http://localhost:8081/user/login")
driver.find_element_by_name('j_username').clear()
driver.find_element_by_name('j_username').send_keys('admin')
# password
driver.find_element_by_css_selector('input[type="password"]').clear()
driver.find_element_by_css_selector('input[type="password"]').send_keys('admin')
driver.find_element_by_class_name('el-button').click()

# 创建项目
driver.get("http://localhost:8081/project/add")
# 项目类型--应收账款
project_type_st = driver.find_element_by_class_name('projectType')
project_type_st.find_element_by_xpath("//option[@value='2']").click()
# 项目名称-- 应收账款
suffix = '星期'+time.strftime('%w', time.localtime())+"_"+str(random.randint(1, 1000))+"的应收账款"
project_name = suffix.decode("utf-8")
driver.find_element_by_class_name('projectName').send_keys(project_name)
project_remark = suffix+"的项目备注"
project_remark = project_remark.decode("utf-8")
driver.find_element_by_class_name('projectRemark').send_keys(project_remark)

# 核心企业查询
# headers = {
#         'Accept': 'application / json, text / javascript, * / *; q = 0.01',
#         'Accept - Encoding': 'gzip, deflate, br',
#         'Accept - Language': 'zh - CN, zh;q = 0.9',
#         'Connection': "keep - alive",
#         'Host': 'investment.my089.com',
#         'Origin': 'https: // investment.my089.com',
#         'Referer':'https: // investment.my089.com / credit',
#         'Content-Type': 'application/x-www-form-urlencoded',
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
# }
# core_enterprise_resp = requests.get('http://localhost:8081/enterprise/getEnterpriseOrPersonByOpenAccount?enterpriseType=CORE&keyword=',headers=headers)
# core_enterprise_resp_json = core_enterprise_resp.text
# core_enterprise_resp_json = core_enterprise_resp_json.encode("utf-8")
# print core_enterprise_resp_json
# 项目来源
core_enterprise = driver.find_element_by_class_name("coreEnterprise")
core_enterprise.clear()
core_enterprise.send_keys(u"开发用测试核心企业")
time.sleep(3)
core_enterprise.click()
p_core_enterprise_best = core_enterprise.find_element_by_xpath("..")
p_core_enterprise_best.find_element_by_css_selector("div>ul>table>tbody").click()

# 还款方
should_loan_enterprise = driver.find_element_by_class_name("shouldLoanEnterprise")
should_loan_enterprise.clear()
should_loan_enterprise.send_keys(u"开发用测试链属企业")
time.sleep(3)
should_loan_enterprise.click()
should_loan_enterprise_best = should_loan_enterprise.find_element_by_xpath("..")
should_loan_enterprise_best.find_element_by_css_selector("div>ul>table>tbody").click()
# 融资方--天津苏日机构投资
should_loan_enterprise = driver.find_element_by_class_name("creditorEnterprise")
should_loan_enterprise.clear()
should_loan_enterprise.send_keys(u"开发用测试链属企业")
time.sleep(3)
should_loan_enterprise.click()
should_loan_enterprise_best = should_loan_enterprise.find_element_by_xpath("..")
should_loan_enterprise_best.find_element_by_css_selector("div>ul>table>tbody").click()
# 用款方信息--useFundEnterprise
useFundEnterprise = driver.find_element_by_class_name("useFundEnterprise")
useFundEnterprise.clear()
useFundEnterprise.send_keys(u"开发用测试链属企业")
time.sleep(3)
useFundEnterprise.click()
useFundEnterprise_best = useFundEnterprise.find_element_by_xpath("..")
useFundEnterprise_best.find_element_by_css_selector("div>ul>table>tbody").click()
# 交易对手方-- 乐山市鹭岛商贸股份有限公司 -coreSubEnterprise

should_loan_enterprise = driver.find_element_by_class_name("coreSubEnterprise")
should_loan_enterprise.clear()
should_loan_enterprise.send_keys(u"乐山市鹭岛商贸股份有限公司")
time.sleep(3)
should_loan_enterprise.click()
should_loan_enterprise_best = should_loan_enterprise.find_element_by_xpath("..")
should_loan_enterprise_best.find_element_by_css_selector("div>ul>table>tbody").click()

# 项目等级
project_level_st = driver.find_element_by_class_name("projectLevel")
project_level_st.find_element_by_xpath("//option[@value='EIGHT']").click()

# 融资金额
driver.find_element_by_class_name('totalAmount').send_keys(1000)
# 投标开始时间
# driver.find_element_by_class_name('pubTime').send_keys('2019-11-15 10:00:00')
# driver.find_element_by_class_name('pubTime').click()
# 投标结束时间
# driver.find_element_by_class_name('bidEndTime').send_keys('2020-11-15 10:00:00')
# 融资期限
driver.find_element_by_id('monthDueTime').find_element_by_xpath('//option[@value="3"]').click()
# 利息/基准管理费/溢价管理费(暂时不设置)
# 是否加入上标管理页
# 是否回购
# 是否支持转让
# 项目所属平台
# 项目所属分区(大中型客户/高净值/中小型)
# 项目状态(创建中/即将开始)
# 超投控制(允许超投/不允许超投)
# 超出授信额度时是否锁定管理费率
# 活动加息
# 资料是否齐备
# 是否自动登记
# 应收应付账款/票据金额
driver.find_element_by_class_name('faceAmount').send_keys(1000)
# ------------------- 融资方信息(逾期情况/所有平台累计融资余额/收入/负债) -------------------
# ------------------- 合同信息 -------------------
contract_name = "c_"+time.strftime("%Y", time.localtime())
contract_name = contract_name.encode("utf-8")
driver.find_element_by_class_name('contractName').send_keys(contract_name)
contract_no = "c_"+time.strftime("%Y%m%d%H%M%S",time.localtime())
contract_no = contract_no.encode("utf-8")
driver.find_element_by_class_name('contractNo').send_keys(contract_no)
driver.find_element_by_class_name('contractAmount').send_keys(1000)
# ------------------- 项目信息 -------------------
# ------------------- 风险保障 -------------------
# ------------------- 投资信息设置 -------------------
value = driver.find_element_by_class_name('minInvestAmt').get_attribute('value')
value = int(value)
maxKeepInvestAmt_input = driver.find_element_by_class_name('maxKeepInvestAmt')
maxKeepInvestAmt_input.clear()
maxKeepInvestAmt_input.send_keys(value)
maxSteadyInvestAmt_input = driver.find_element_by_class_name('maxSteadyInvestAmt')
maxSteadyInvestAmt_input.clear()
maxSteadyInvestAmt_input.send_keys(value)
maxPositiveInvestAmt_input = driver.find_element_by_class_name('maxPositiveInvestAmt')
maxPositiveInvestAmt_input.clear()
maxPositiveInvestAmt_input.send_keys(value*2)
# ------------------- 提交保存 -------------------
# 保存
driver.find_element_by_class_name('add-save').click()
# 捕获alert
alert = driver.switch_to.alert
alert.accept()
