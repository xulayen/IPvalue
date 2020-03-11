import unittest
from common.fuction import *
#叶子节点权重值为空，点击确定按钮报错提示（数值不为空）
ipMethod = method()
class Testson_comf(unittest.TestCase):
    def test_01(self):
        action()
        inputValuefull(attr[0], ele_level1_3, valuelevel1_3["name"], valueemptyqz1_3['qz'], valueemptyqz1_3['sz'])
        time.sleep(3)
        alert = ipMethod.driver.switch_to.alert
        # print(alert.text)
        assert '请输入数字格式' in alert.text

        # 查询点击弹框确定按钮后 报错提示去除
        alert.accept()



