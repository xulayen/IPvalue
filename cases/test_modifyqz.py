import unittest
from common.fuction import *
ipMethod = method()
class Testmodifyqz(unittest.TestCase):
#'ip价值评估正常场景2-修改权重，权重值加起来小于1，应有提示'
    def test_01(self):
        action()
        inputValuefull(attr[0], ele_level1_3, valuelevel1_3["name"], valuelevel1_3['qz'], valuelevel1_3['sz'])
        modifyQz(attr[0], ele_level1_3, small_value1_3)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(3)
        alert = ipMethod.driver.switch_to.alert
        assert '节点权重值之和不为1' in alert.text
        alert.accept()







# 'ip价值评估正常场景2-修改权重，权重值加起来大于1，应有提示'
    def test_02(self):
            action()
            inputValuefull(attr[0], ele_level1_3, valuelevel1_3["name"], valuelevel1_3['qz'], valuelevel1_3['sz'])
            modifyQz(attr[0], ele_level1_3, value1_3)
            ipMethod.click(attr[0], menu_calcubtn)
            time.sleep(3)
            alert = ipMethod.driver.switch_to.alert
            assert '目前权重值之和超过了1' in alert.text
            alert.accept()




# 修改权重值和仍为1
    def test_03(self):
        action()
        inputValuefull(attr[0], ele_level1_3, valuelevel1_3["name"], valuelevel1_3['qz'], valuelevel1_3['sz'])
        modifyQz(attr[0], ele_level1_3, small_value1_3)
        modifyQz(attr[0], ele_level1_2, small_value1_2)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(3)
        text_total = ipMethod.getvalue(attr[0], after_resm_total, 'innerHTML')
        text_1 = ipMethod.getvalue(attr[1], resm_1, 'innerHTML')
        assert text_total == '6.55'
        assert text_1 == '22.0'







# 权重值为负数，应有报错提示
    def test_04(self):
        action()
        inputValuefull(attr[0], ele_level1_3, valuelevel1_3["name"], negative_value1_3, valuelevel1_3['sz'])
        time.sleep(3)
        alert=ipMethod.driver.switch_to.alert
        assert '请输入数字格式' in alert.text
        alert.accept()




#权重值带有字母，应有报错提示

    def test_05(self):
        action()
        inputValuefull(attr[0], ele_level1_3, valuelevel1_3["name"], letter_value1_3, valuelevel1_3['sz'])
        time.sleep(3)
        alert = ipMethod.driver.switch_to.alert
        assert '请输入数字格式' in alert.text
        alert.accept()






