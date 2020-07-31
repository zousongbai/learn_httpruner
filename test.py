# -*- coding:utf-8 -*-
# @Author       : 小青年
# @ProjectName  :learn_httprunner
# @File         : test.py
# @Time         : 2020/7/31 9:55

# （1）步骤一从httprunner导入HttpRunner
from httprunner.api import HttpRunner
# （2）步骤二：定义HttpRunner对象
hrunner=HttpRunner()
# （3）步骤三：运行yml的配置文件：使用HttpRunner对象中的run方法，参数是执行文件的路径
hrunner.run(r'D:\study\project\ck04\Django\learn_httprunner\testsuites\api_testsuite.yml')

# （4）步骤四：获取执行结果：　
print(hrunner.summary)