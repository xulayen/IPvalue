import unittest
from common.fuction import *
ipMethod=method()
class Testmodifysz(unittest.TestCase):
    def test_01(self):
        u'''ip价值评估正常场景2-一个叶子节点修改数值'''
        action()
        inputValuefull(attr[0], ele_level1_3, valuelevel1_3["name"], valuelevel1_3['qz'], valuelevel1_3['sz'])
        # 点击确认计算总值
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(8)
        text_total = ipMethod.getvalue(attr[0], resm_total, 'innerHTML')
        print(text_total)
        text_1 = ipMethod.getvalue(attr[1], resm_1, 'innerHTML')
        text_2 = ipMethod.getvalue(attr[1], resm_2, 'innerHTML')
        text_3 = ipMethod.getvalue(attr[1], resm_3, 'innerHTML')
        text_4 = ipMethod.getvalue(attr[1], resm_4, 'innerHTML')
        text_5 = ipMethod.getvalue(attr[1], resm_5, 'innerHTML')

        text_1_1 = ipMethod.getvalue(attr[1], resm_1_1, 'innerHTML')
        text_1_2 = ipMethod.getvalue(attr[1], resm_1_2, 'innerHTML')
        text_1_3 = ipMethod.getvalue(attr[1], resm_1_3, 'innerHTML')
        tuple = (text_total, text_1, text_2, text_3, text_4, text_5, text_1_1, text_1_2, text_1_3)
        print(tuple)

        tuple1 = (
            dict2["final_total"], dict2["final_1"], dict2["final_2"], dict2["final_3"], dict2["final_4"],
            dict2["final_5"]
            , dict2["final_1_1"], dict2["final_1_2"], dict2["final_1_3"])
        print(tuple1)
        assert tuple == tuple1
        # 修改
        modifySz(attr[0], xpath1_3, 20)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(2)
        after_text_total = ipMethod.getvalue(attr[0], after_resm_total, 'innerHTML')
        after_text_1_3 = ipMethod.getvalue(attr[1], after_resm_1_3, 'innerHTML')
        print(after_text_total, type(after_text_total))
        assert after_text_total == '5.75'
        assert after_text_1_3 == '20'


    def test_02(self):
        u'''#节点数值删除，能成功删除'''
        action()
        inputValuefull(attr[0], ele_level1_3, valuelevel1_3["name"], valuelevel1_3['qz'], valuelevel1_3['sz'])
        # 点击确认计算总值
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(3)
        modifySz(attr[0], xpath1_3, '')
        ipMethod.ac_click(attr[0], value_top)
        ipMethod.ac_click(attr[0], xpath1_3)
        sz_1_3 = ipMethod.getvalue(attr[0], menu_countvalue, 'value')
        print(sz_1_3)
        assert sz_1_3 == ''





    # #数值为字母
    # def test_03(self):
    #     action()
    #     inputValuefull(attr[0], ele_level1_3, valuelevel1_3["name"], valuelevel1_3['qz'], valuelevel1_3['sz'])
    #     modifySz(attr[0], ele_level1_3, letter_value1_3)
    #     ipMethod.click(attr[0], menu_calcubtn)
    #     time.sleep(3)
    #     alert = ipMethod.driver.switch_to.alert
    #     assert '数值' in alert.text
    #     alert.accept()





    def test_04(self):
        u'''#数值为负数'''
        action()
        inputValuefull(attr[0], ele_level1_3, valuelevel1_3["name"], valuelevel1_3['qz'], valuelevel1_3['sz'])
        modifySz(attr[0], ele_level1_3, negative_value1_3)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(3)
        text_total=ipMethod.getvalue(attr[0],resm_total,'innerHTML')
        assert text_total=='3.7'










