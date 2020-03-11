
import unittest
from common.fuction import *
ipMethod = method()
#父节点为空，直接点击计算总值，报错提示（数值也为空，相当于该节点没有编辑）
class Testpar_eva(unittest.TestCase):
    def test_01(self):
        action1()
        # 点击确认计算总值
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(3)
        alert = ipMethod.driver.switch_to.alert
        # print(alert.text)
        assert ('权重值未填写') in alert.text
        # 查询点击弹框确定按钮后 报错提示去除
        alert.accept()








# #父节点数值为空，点击确定成功保存   -----父节点数值为空，点击确定成功保存，点击计算总值，可计算（权重不为空）
    def test_02(self):
        action1()
        inputValuefull(attr[0], levelvalue[0], level1_value["name"], level1_value['qz'], level1_value['sz'])
        # 点击确认计算总值
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(3)
        text_total = ipMethod.getvalue(attr[0], level_total_value, 'innerHTML')
        assert text_total == '8.15'









