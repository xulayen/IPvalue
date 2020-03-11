#叶子节点数值为空，点击确定不报错——数值为空点击确定点击计算总值报错  （权重不为空）
import unittest
from common.fuction import *
ipMethod = method()
class Testson_sz_eva(unittest.TestCase):
    def test_01(self):
        action()
        inputValuefull(attr[0], ele_level1_3, valuelevel1_3["name"], valueemptysz1_3['qz'], valueemptysz1_3['sz'])
        # 点击确认计算总值
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(3)
        alert = ipMethod.driver.switch_to.alert
        # print(alert.text)
        assert ('数值或者权重值未填写') in alert.text

        # 查询点击弹框确定按钮后 报错提示去除
        alert.accept()

        ##查询错误弹框确定后，计算接口未调用
        after_text_1 = ipMethod.getvalue(attr[1], empty_resm_1, 'innerHTML')
        print(after_text_1)
        assert after_text_1 == '1'



