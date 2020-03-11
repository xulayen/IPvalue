from common.base import *
from test_data.test_data import *
ipMethod=method()

def top(ele_attri,loc):
    ipMethod.contentclick(ele_attri,loc)
    time.sleep(2)
    ipMethod.click(ele_attri, value_down)



def inputValuefull(ele_attri,ele_level,namevalue,qzvalue,countvalue):
    time.sleep(1)
    ipMethod.ac_click(ele_attri,ele_level)
    ipMethod.clear(ele_attri,menu_name)
    ipMethod.sendkeys(ele_attri,menu_name,namevalue)
    ipMethod.sendkeys(ele_attri, menu_countvalue, countvalue)
    ipMethod.sendkeys(ele_attri,menu_qzcount,qzvalue)
    ipMethod.click(ele_attri,menu_confirmbtn)


def modifySz(ele_attri,ele_level,countvalue):
    time.sleep(1)
    ipMethod.ac_click(ele_attri,ele_level)
    ipMethod.clear(ele_attri,menu_countvalue)
    ipMethod.sendkeys(ele_attri, menu_countvalue, countvalue)
    ipMethod.click(ele_attri,menu_confirmbtn)

def modifyQz(ele_attri,ele_level,qzvalue):
    time.sleep(1)
    ipMethod.ac_click(ele_attri,ele_level)
    ipMethod.clear(ele_attri,menu_qzcount)
    ipMethod.sendkeys(ele_attri, menu_qzcount, qzvalue)
    ipMethod.click(ele_attri,menu_confirmbtn)


def modifyCon(ele_attri,ele_level,con):
    time.sleep(1)
    ipMethod.ac_click(ele_attri,ele_level)
    ipMethod.clear(ele_attri,menu_name)
    ipMethod.sendkeys(ele_attri, menu_name, con)
    ipMethod.click(ele_attri,menu_confirmbtn)


#叶子节点修改值
def action():
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
    inputValuefull(attr[0], ele_level1_1, valuelevel1_1["name"], valuelevel1_1['qz'], valuelevel1_1['sz'])
    inputValuefull(attr[0], ele_level1_2, valuelevel1_2["name"], valuelevel1_2['qz'], valuelevel1_2['sz'])



#父节点修改值
def action1():
    ipMethod.open()
    ipMethod.maximize()
    time.sleep(2)
    for i in range(1, 6):
        top(attr[0], value_top)

    time.sleep(3)
    # 节点2，节点3，节点4，节点5的值输入
    inputValuefull(attr[0], levelvalue[1], valuelevel2["name"], valuelevel2['qz'], valuelevel2['sz'])
    inputValuefull(attr[0], levelvalue[2], valuelevel3["name"], valuelevel3['qz'], valuelevel3['sz'])
    inputValuefull(attr[0], levelvalue[3], valuelevel4["name"], valuelevel4['qz'], valuelevel4['sz'])
    inputValuefull(attr[0], levelvalue[4], valuelevel5["name"], valuelevel5['qz'], valuelevel5['sz'])

    # 子节点的叶子节点创建
    top(attr[0], levelvalue[0])
    inputValuefull(attr[0], level1_1_ele, level1_1_value["name"], level1_1_value['qz'], level1_1_value['sz'])

