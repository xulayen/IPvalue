from common.base import method
from test_data.test_data import *



newmethod=method()
attr={'xpath','css_selector'}

#根节点的元素定位
value_top_ele=newmethod.find_element(attr[0],value_top)

#下级按钮元素 定位
value_down_ele=newmethod.find_element(attr[0],value_top)


#节点1定位/节点2定位/节点3定位/节点4定位/节点5定位
level1_ele=newmethod.find_element(attr[0],levelvalue[0])
level2_ele=newmethod.find_element(attr[0],levelvalue[1])
level3_ele=newmethod.find_element(attr[0],levelvalue[2])
level4_ele=newmethod.find_element(attr[0],levelvalue[3])
level5_ele=newmethod.find_element(attr[0],levelvalue[4])


#叶子节点元素定位
level1_1_ele=newmethod.find_element(attr[0],ele_level1_1)
level1_2_ele=newmethod.find_element(attr[0],ele_level1_2)
level1_3_ele=newmethod.find_element(attr[0],ele_level1_3)

level2_1_ele=newmethod.find_element(attr[0],ele_level2_1)
level2_2_ele=newmethod.find_element(attr[0],ele_level2_2)
level2_3_ele=newmethod.find_element(attr[0],ele_level2_3)
level2_4_ele=newmethod.find_element(attr[0],ele_level2_4)
level2_5_ele=newmethod.find_element(attr[0],ele_level2_5)

level3_1_ele=newmethod.find_element(attr[0],ele_level3_1)
level3_2_ele=newmethod.find_element(attr[0],ele_level3_2)
level4_1_ele=newmethod.find_element(attr[0],ele_level4_1)

level3_2_1_ele=newmethod.find_element(attr[0],ele_level3_2_1)
level3_2_2_ele=newmethod.find_element(attr[0],ele_level3_2_2)



#数值属性布局里属性定位
menu_name_ele = newmethod.find_element(attr[0],menu_name)
menu_qzcount_ele = newmethod.find_element(attr[0],menu_qzcount)
menu_confirmbtn_ele =newmethod.find_element(attr[0],menu_confirmbtn)
menu_calcubtn_ele=newmethod.find_element(attr[0],menu_calcubtn)



#各节点上数值显示元素定位

res_total_ele=newmethod.find_element(attr[1],res_total)

res_1_ele=newmethod.find_element(attr[1],res_1)
res_2_ele=newmethod.find_element(attr[1],res_2)
res_3_ele=newmethod.find_element(attr[1],res_3)
res_4_ele=newmethod.find_element(attr[1],res_4)
res_5_ele=newmethod.find_element(attr[1],res_5)

res_1_1_ele=newmethod.find_element(attr[1],res_1_1)
res_1_2_ele=newmethod.find_element(attr[1],res_1_2)
res_1_3_ele=newmethod.find_element(attr[1],res_1_3)

res_2_1_ele=newmethod.find_element(attr[1],res_2_1)
res_2_2_ele=newmethod.find_element(attr[1],res_2_2)
res_2_3_ele=newmethod.find_element(attr[1],res_2_3)
res_2_4_ele=newmethod.find_element(attr[1],res_2_4)
res_2_5_ele=newmethod.find_element(attr[1],res_2_5)

res_3_1_ele=newmethod.find_element(attr[1],res_3_1)
res_3_2_ele=newmethod.find_element(attr[1],res_3_2)
res_3_2_1_ele=newmethod.find_element(attr[1],res_3_2_1)
res_3_2_2_ele=newmethod.find_element(attr[1],res_3_2_2)
res_4_1_ele=newmethod.find_element(attr[1],res_4_1)


# tuple=(text_total,text_1,text_2,text_3,text_4,text_5,text_1_1,text_1_2,text_1_3,text_2_1,text_2_2,text_2_3,text_2_4,text_2_5,text_3_1,text_3_2,text_3_2_1,text_3_2_2,text_4_1)
# tuple1=('15.32','23.0','36.25','26.28','10.0','10','10','20','30','10','20','30','40','50','10','37.14','30','40','10')
#
# assert tuple==tuple1


























