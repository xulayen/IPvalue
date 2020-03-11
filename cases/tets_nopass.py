import unittest
from common.fuction import *
ipMethod=method()
#正常输入数值，权重；分支被有一节点一票否决,计算总值为0
class Testnopass(unittest.TestCase):
    def test_01(self):
        action()
        inputValuefull(attr[0], ele_level1_3, valuelevel1_3["name"], valuelevel1_3['qz'], valuelevel1_3['sz'])
        # 点击确认计算总值
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(8)
        ipMethod.ac_click(attr[0], xpath1_3)
        ipMethod.click(attr[0], menu_nopass)
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(2)
        text_total = ipMethod.getvalue(attr[0], after_resm_total, 'innerHTML')
        text_1 = ipMethod.getvalue(attr[1], after_resm_1, 'innerHTML')
        print(text_total, text_1)
        assert text_total == '0.0'
        assert text_1 == '0.0'


# # #父节点测试1不参与计算，其下分支1.3被否决，仍优先一票否决
    def test_02(self):
        action()
        inputValuefull(attr[0], ele_level1_3, valuelevel1_3["name"], valuelevel1_3['qz'], valuelevel1_3['sz'])
        ipMethod.click(attr[0], ele_level1_3)
        ipMethod.click(attr[0], menu_nopass)
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], levelvalue[0])
        ipMethod.click(attr[0], menu_noselect)
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(2)
        text_total = ipMethod.getvalue(attr[0], after_resm_total, 'innerHTML')
        text_1 = ipMethod.getvalue(attr[1], after_resm_1, 'innerHTML')
        print(text_total, text_1)
        assert text_total == '0.0'
        assert text_1 == '0.0'


#父节点分支测试1被否决，分支1.3 不参与计算；计算总值为0
    def test_03(self):
        action()
        inputValuefull(attr[0], ele_level1_3, valuelevel1_3["name"], valuelevel1_3['qz'], valuelevel1_3['sz'])
        ipMethod.click(attr[0], ele_level1_3)
        ipMethod.click(attr[0], menu_noselect)
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], levelvalue[0])
        ipMethod.click(attr[0], menu_nopass)
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(2)
        text_total = ipMethod.getvalue(attr[0], after_resm_total, 'innerHTML')
        text_1 = ipMethod.getvalue(attr[1], after_resm_1, 'innerHTML')
        print(text_total, text_1)
        assert text_total == '0.0'
        assert text_1 == '8.0'



#一票否决被反选
    def test_04(self):
        action()
        inputValuefull(attr[0], ele_level1_3, valuelevel1_3["name"], valuelevel1_3['qz'], valuelevel1_3['sz'])
        # 点击确认计算总值
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(8)
        ipMethod.ac_click(attr[0], xpath1_3)
        ipMethod.click(attr[0], menu_nopass)
        ipMethod.click(attr[0], menu_nopass)
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(2)
        text_total = ipMethod.getvalue(attr[0], after_resm_total, 'innerHTML')
        text_1 = ipMethod.getvalue(attr[1], after_resm_1, 'innerHTML')
        print(text_total, text_1)
        assert text_total == '6.75'
        assert text_1 == '23.0'








#权重值和不等于1，其中有节点被一票否决，仍应提示权重和不等于1
    def test_05(self):
        action()
        inputValuefull(attr[0], ele_level1_3, valuelevel1_3["name"], small_value1_3, valuelevel1_3['sz'])
        ipMethod.ac_click(attr[0], levelvalue[0])
        ipMethod.click(attr[0], menu_nopass)
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(2)
        alert = ipMethod.driver.switch_to.alert
        print(alert.text)
        assert '节点权重值之和不为1' in alert.text






