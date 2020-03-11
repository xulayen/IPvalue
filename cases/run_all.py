
import unittest
import os
import time


from BeautifulReport import BeautifulReport

# 获取当前目录路径
casepath = './'

def add_case(case_path=casepath, rule="*test*.py"):
    '''加载所有的测试用例'''
    discover = unittest.defaultTestLoader.discover(case_path,pattern=rule,top_level_dir=None)
    return discover


def run_case(all_case):
    '''执行所有的用例, 并把结果写入测试报告'''
    result = BeautifulReport(all_case)
    path = os.path.abspath('..')
    finalpath = path + "\Report"
    #nowday = time.strftime('%Y%m%d%H%M', time.localtime())
    #filename='ip价值评估测试报告'+nowday
    result.report(filename="ip价值评估测试报告", description="", log_path=finalpath)




if __name__ == "__main__":
    # 用例集合
    cases = add_case()
    for i  in cases:
        print(i)
        run_case(i)

####