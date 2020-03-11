#数值，权重，标题修改后未点击确定，点击计算总值,计算总值应该不变
import unittest
from common.fuction import *
class notSave(unittest.TestCase):
    def test_01(self):
        action()
        inputValuefull(attr[0], ele_level1_3, valuelevel1_3["name"], valuelevel1_3['qz'], valuelevel1_3['sz'])
        # 点击确认计算总值
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(3)
        text_total = ipMethod.getvalue(attr[0], resm_total, 'innerHTML')
        ipMethod.ac_click(attr[0], xpath1_3)
        ipMethod.clear(attr[0], menu_name)
        ipMethod.sendkeys(attr[0], menu_name, notsave_1_3['name'])
        ipMethod.clear(attr[0], menu_qzcount)
        ipMethod.sendkeys(attr[0], menu_qzcount, notsave_1_3['qz'])
        ipMethod.clear(attr[0], menu_countvalue)
        ipMethod.sendkeys(attr[0], menu_countvalue, notsave_1_3['sz'])
        ipMethod.click(attr[0], menu_calcubtn)
        text_total1 = ipMethod.getvalue(attr[0], resm_total, 'innerHTML')
        assert text_total == text_total1



##