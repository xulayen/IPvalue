import unittest
from common.fuction import *
ipMethod=method()
class Testselecteva(unittest.TestCase):
    def test_01(self):
        # 父节点下3个节点，其中分支下两节点参与计算
        action()
        inputValuefull(attr[0], ele_level1_3, valuelevel1_3["name"], valuelevel1_3['qz'], valuelevel1_3['sz'])
        ipMethod.ac_click(attr[0], ele_level1_3)
        ipMethod.click(attr[0], menu_noselect)
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(2)
        text_total = ipMethod.getvalue(attr[0], after_resm_total, 'innerHTML')
        text_1 = ipMethod.getvalue(attr[1], resm_1, 'innerHTML')
        assert text_total == '3.75'
        assert text_1 == '8.0'


    def test_02(self):
        # 父节点测试1不参与计算
        action()
        inputValuefull(attr[0], ele_level1_3, valuelevel1_3["name"], valuelevel1_3['qz'], valuelevel1_3['sz'])
        ipMethod.ac_click(attr[0], levelvalue[0])
        ipMethod.click(attr[0], menu_noselect)
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        text_total = ipMethod.getvalue(attr[0], after_resm_total, 'innerHTML')
        text_1 = ipMethod.getvalue(attr[1], resm_1, 'innerHTML')
        assert text_total == '2.15'
        assert text_1 == '23.0'



    def test_03(self):
        # 父节节点权重和为1，子节点权重和不为1，父节点选择不参与计算，应有报错提示
        action()
        inputValuefull(attr[0], ele_level1_3, valuelevel1_3["name"], small_value1_3, valuelevel1_3['sz'])
        ipMethod.ac_click(attr[0], levelvalue[0])
        ipMethod.click(attr[0], menu_noselect)
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(2)
        alert = ipMethod.driver.switch_to.alert
        print(alert.text)
        assert '节点权重值之和不为1' in alert.text



