
from cases.test_evaute import *
from cases.test_modify_nosave import *
from cases.test_modifyconent import *
from cases.test_modifyqz import *
from cases.test_modifysz import *
from cases.test_parempty_comf import *
from cases.test_parempty_eva import *
from cases.test_selecteva import *
from cases.test_sonempty_comf import *
from cases.test_sonempty_evaqz import *
from cases.tets_nopass import *
from HTMLTestRunner import HTMLTestRunner
from datetime  import date
from BeautifulReport import BeautifulReport
from unittest import defaultTestLoader
import os
case_path =os.getcwd()
print(case_path)



#
# def get_allcase():
#     discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")
#     testsuite = unittest.TestSuite()
#     testsuite.addTest(discover)
#     return testsuite
#
#
#
# #这个方法适用于执行少量测试用例，需要手动一个一个addTest去加载，
# # 如果一个类下面有很多测试用例会比较麻烦，这时候我们需要makeSuite()方法，下一篇我们接着讲
# # suite.addTest(unittest.makeSuite(TestLogin))  # 一次记载多个用例
# if __name__ == '__main__':
#     #单个用例执行
#     filename = '../result/htmlreport'+str(date.today())+'.html'
#     ftp =  open(filename, 'wb')
#     runner=HTMLTestRunner(stream=ftp,title='test report',description='report')
#     runner.run(get_allcase())






if __name__ == '__main__':
    #单个用例执行
    suite = unittest.TestSuite()
    suite.addTest(Testmodifysz('test_04'))
    filename = '../result/htmlreport'+str(date.today())+'.html'
    ftp =  open(filename, 'wb')
    runner=HTMLTestRunner(stream=ftp,title='test report',description='report')
    runner = unittest.TextTestRunner()
    runner.run(suite)
