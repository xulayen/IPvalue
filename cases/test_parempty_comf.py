
import unittest
from common.fuction import *
ipMethod = method()
#父节的权重为空,点击确定会报错提示（数值不为空）
class Testparcomf(unittest.TestCase):
    def test_01(self):
        action1()
        # 父节点1的数值输入点击确定
        inputValuefull(attr[0], levelvalue[0], level1_value1["name"], level1_value1['qz'], level1_value1['sz'])
        time.sleep(2)
        alert = ipMethod.driver.switch_to.alert
        assert '请输入数字格式' in alert.text
        alert.accept()




#数值输入带有字母应有判断，此提示还未开发


#父节点的权重不为空，数值为空，点击确定成功保存 这个场景已被"权重不为空，数值为空 点击确定-点击计算总值"(已覆盖）

















