import unittest
from common.fuction import *
ipMethod=method()
class Testevaute(unittest.TestCase):
# 'ip价值评估正常场景-计算（权重相加为1，全为正数）,负数的情况还没有写'
    def test_01(self):
        ipMethod.open()
        ipMethod.maximize()
        time.sleep(2)

        for i in range(1, 6):
            top(attr[0], value_top)

        time.sleep(3)
        # 节点1，节点2，节点3，节点4，节点5的值输入
        inputValuefull(attr[0], levelvalue[0], valuelevel1["name"], valuelevel1['qz'], valuelevel1['sz'])
        inputValuefull(attr[0], levelvalue[1], valuelevel2["name"], valuelevel2['qz'], valuelevel2['sz'])
        inputValuefull(attr[0], levelvalue[2], valuelevel3["name"], valuelevel3['qz'], valuelevel3['sz'])
        inputValuefull(attr[0], levelvalue[3], valuelevel4["name"], valuelevel4['qz'], valuelevel4['sz'])
        inputValuefull(attr[0], levelvalue[4], valuelevel5["name"], valuelevel5['qz'], valuelevel5['sz'])

        # 子节点的叶子节点创建
        for i in range(0, 4):
            n = 0
            time.sleep(2)
            if i == 0:
                for n in range(1, 4):
                    top(attr[0], levelvalue[i])
            elif i == 1:
                for n in range(1, 6):
                    top(attr[0], levelvalue[i])
            elif i == 2:
                for n in range(1, 3):
                    top(attr[0], levelvalue[i])
                    time.sleep(3)
            elif i == 3:
                for n in range(1, 2):
                    top(attr[0], levelvalue[i])

        for i in range(1, 3):
            top(attr[0], ele_level3_2)

        inputValuefull(attr[0], ele_level1_1, valuelevel1_1["name"], valuelevel1_1['qz'], valuelevel1_1['sz'])
        inputValuefull(attr[0], ele_level1_2, valuelevel1_2["name"], valuelevel1_2['qz'], valuelevel1_2['sz'])
        inputValuefull(attr[0], ele_level1_3, valuelevel1_3["name"], valuelevel1_3['qz'], valuelevel1_3['sz'])

        inputValuefull(attr[0], ele_level2_1, valuelevel2_1["name"], valuelevel2_1['qz'], valuelevel2_1['sz'])
        inputValuefull(attr[0], ele_level2_2, valuelevel2_2["name"], valuelevel2_2['qz'], valuelevel2_2['sz'])

        inputValuefull(attr[0], ele_level2_3, valuelevel2_3["name"], valuelevel2_3['qz'], valuelevel2_3['sz'])
        inputValuefull(attr[0], ele_level2_4, valuelevel2_4["name"], valuelevel2_4['qz'], valuelevel2_4['sz'])
        inputValuefull(attr[0], ele_level2_5, valuelevel2_5["name"], valuelevel2_5['qz'], valuelevel2_5['sz'])
        inputValuefull(attr[0], ele_level3_1, valuelevel3_1["name"], valuelevel3_1['qz'], valuelevel3_1['sz'])
        inputValuefull(attr[0], ele_level3_2, valuelevel3_2["name"], valuelevel3_2['qz'], valuelevel3_2['sz'])
        inputValuefull(attr[0], ele_level3_2_1, valuelevel3_2_1["name"], valuelevel3_2_1['qz'], valuelevel3_2_1['sz'])
        inputValuefull(attr[0], ele_level3_2_2, valuelevel3_2_2["name"], valuelevel3_2_2['qz'], valuelevel3_2_2['sz'])
        inputValuefull(attr[0], ele_level4_1, valuelevel_4_1["name"], valuelevel_4_1['qz'], valuelevel_4_1['sz'])

        # 点击确认计算总值
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(8)

        # 获取各个节点上的值
        text_total = ipMethod.getvalue(attr[0], res_total, 'innerHTML')
        print(text_total)
        text_1 = ipMethod.getvalue(attr[1], res_1, 'innerHTML')
        text_2 = ipMethod.getvalue(attr[1], res_2, 'innerHTML')
        text_3 = ipMethod.getvalue(attr[1], res_3, 'innerHTML')
        text_4 = ipMethod.getvalue(attr[1], res_4, 'innerHTML')
        text_5 = ipMethod.getvalue(attr[1], res_5, 'innerHTML')

        text_1_1 = ipMethod.getvalue(attr[1], res_1_1, 'innerHTML')
        text_1_2 = ipMethod.getvalue(attr[1], res_1_2, 'innerHTML')
        text_1_3 = ipMethod.getvalue(attr[1], res_1_3, 'innerHTML')
        text_2_1 = ipMethod.getvalue(attr[1], res_2_1, 'innerHTML')
        text_2_2 = ipMethod.getvalue(attr[1], res_2_2, 'innerHTML')
        text_2_3 = ipMethod.getvalue(attr[1], res_2_3, 'innerHTML')
        text_2_4 = ipMethod.getvalue(attr[1], res_2_4, 'innerHTML')
        text_2_5 = ipMethod.getvalue(attr[1], res_2_5, 'innerHTML')

        text_3_1 = ipMethod.getvalue(attr[1], res_3_1, 'innerHTML')
        text_3_2 = ipMethod.getvalue(attr[1], res_3_2, 'innerHTML')
        text_3_2_1 = ipMethod.getvalue(attr[1], res_3_2_1, 'innerHTML')
        text_3_2_2 = ipMethod.getvalue(attr[1], res_3_2_2, 'innerHTML')
        text_4_1 = ipMethod.getvalue(attr[1], res_4_1, 'innerHTML')

        tuple = (
            text_total, text_1, text_2, text_3, text_4, text_5, text_1_1, text_1_2, text_1_3, text_2_1, text_2_2,
            text_2_3,
            text_2_4, text_2_5, text_3_1, text_3_2, text_3_2_1, text_3_2_2, text_4_1)

        tuple1 = (
            dict1["final_total"], dict1["final_1"], dict1["final_2"], dict1["final_3"], dict1["final_4"],
            dict1["final_5"]
            , dict1["final_1_1"], dict1["final_1_2"], dict1["final_1_3"]
            , dict1["final_2_1"], dict1["final_2_2"], dict1["final_2_3"], dict1["final_2_4"], dict1["final_2_5"],
            dict1["final_3_1"], dict1["final_3_2"], dict1["final_3_2_1"], dict1["final_3_2_2"], dict1["final_4_1"])
        print(tuple, tuple)
        assert tuple == tuple











































