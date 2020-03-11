import unittest
from common.fuction import *
ipMethod = method()
class Testmodifycon(unittest.TestCase):


#叶子节点内容为空，点击确定，计算总值不受影响
    def test_01(self):
        action()
        inputValuefull(attr[0], ele_level1_3, valueemptycon1_3["name"], valueemptycon1_3['qz'], valueemptycon1_3['sz'])

        # 点击确认计算总值
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(3)
        text_total = ipMethod.getvalue(attr[0], resm_total, 'innerHTML')
        assert text_total == '6.75'





    # 叶子节点的标题内容更改后，能成功更改，且计算值不受影响

    def test_02(self):
        action()
        inputValuefull(attr[0], ele_level1_3, valuelevel1_3["name"], valuelevel1_3['qz'], valuelevel1_3['sz'])

        # 点击确认计算总值
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(3)
        text_total = ipMethod.getvalue(attr[0], resm_total, 'innerHTML')
        assert text_total == '6.75'
        time.sleep(2)
        modifyCon(attr[0], xpath1_3, emptycon1_3['name'])
        text_con_1_3 = ipMethod.getvalue(attr[0], xpath1_3, 'innerHTML')
        assert text_con_1_3 == emptycon1_3["name"]


    #叶子节点的标题内容能够成功删除
    def test03(self):
        action()
        inputValuefull(attr[0], ele_level1_3, valuelevel1_3["name"], valuelevel1_3['qz'], valuelevel1_3['sz'])
        # 点击确认计算总值
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(3)
        modifyCon(attr[0], xpath1_3, '')
        ipMethod.click(attr[0], menu_calcubtn)
        ipMethod.ac_click(attr[1], after_resm_1_3)
        name_1_3 = ipMethod.getvalue(attr[0], menu_name, 'value')
        assert name_1_3 == ''




