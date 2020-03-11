#叶子节点权重为空直接点击计算总值，需报错（数值也为空）
import unittest
from common.fuction import *
ipMethod = method()
class Testson_qz_eva(unittest.TestCase):
    def test_01(self):
        action()
        # 点击确认计算总值
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(3)
        alert = ipMethod.driver.switch_to.alert
        # print(alert.text)
        assert ('数值或者权重值未填写') in alert.text

        # 查询点击弹框确定按钮后 报错提示去除
        alert.accept()

        ##查询错误弹框确定后，计算接口未调用
        after_text_1_3 = ipMethod.getvalue(attr[1], empty_resm_1, 'innerHTML')
        print(after_text_1_3)
        assert after_text_1_3 == '1'

