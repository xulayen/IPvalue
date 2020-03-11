from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

##################################################公用数据######################################
attr=['xpath','css selector']
#根节点的元素定位
value_top="//*[@id='kity_text_22']"

#下级按钮元素 定位
value_down="/html/body/div[1]/div[3]/div[2]/div[1]/div[3]/div[2]/span[1]"


#节点1/节点2，节点3，节点4，节点5，
levelvalue=["//*[@id='kity_text_33']","//*[@id='kity_text_41']","//*[@id='kity_text_49']","//*[@id='kity_text_57']","//*[@id='kity_text_65']"]


#二级节点值
valuelevel1={"name":"分支测试1","qz":'0.2',"sz":1}
valuelevel2={"name":"分支测试2","qz":'0.3',"sz":1}
valuelevel3={"name":"分支测试3","qz":'0.05',"sz":1}
valuelevel4={"name":"分支测试4","qz":'0.3',"sz":1}
valuelevel5={"name":"分支测试5","qz":'0.15',"sz":10}



#三级节点值
valuelevel1_1={"name":"分支1.1","qz":'0.2',"sz":10}
valuelevel1_2={"name":"分支1.2","qz":'0.3',"sz":20}
valuelevel1_3={"name":"分支1.3","qz":'0.5',"sz":30}

valuelevel2_1={"name":"分支2.1","qz":'0.2',"sz":10}
valuelevel2_2={"name":"分支2.2","qz":'0.3',"sz":20}
valuelevel2_3={"name":"分支2.3","qz":'0.05',"sz":30}
valuelevel2_4={"name":"分支2.4","qz":'0.3',"sz":40}
valuelevel2_5={"name":"分支2.5","qz":'0.15',"sz":50}

valuelevel3_1={"name":"分支3.1","qz":'0.2',"sz":10}
valuelevel3_2={"name":"分支3.2","qz":'0.8',"sz":''}
valuelevel_4_1={"name":"分支4.1","qz":'1',"sz":10}

#四级节点值
valuelevel3_2_1={"name":"分支3.2.1","qz":'0.5',"sz":30}
valuelevel3_2_2={"name":"分支3.2.2","qz":'0.5',"sz":40}



#数值属性布局里属性定位
menu_name = '//*[@id="node-menu"]/ul/li[1]/input'
menu_countvalue = "//*[@id='node-menu']/ul/li[2]/input"
menu_qzcount = "//*[@id='node-menu']/ul/li[3]/input"
menu_confirmbtn = "//*[@id='node-menu']/button"
menu_calcubtn='//*[@id="compute"]'
menu_nopass='//*[@id="reject"]'
menu_noselect='//*[@id="uselessWeight"]'

#叶子节点定位

ele_level1_1="//*[@id='kity_text_93']"

ele_level1_2="//*[@id='kity_text_101']"
ele_level1_3="//*[@id='kity_text_109']"
ele_level2_1="//*[@id='kity_text_117']"
ele_level2_2="//*[@id='kity_text_125']"
ele_level2_3="//*[@id='kity_text_133']"

ele_level2_4="//*[@id='kity_text_141']"
ele_level2_5="//*[@id='kity_text_149']"
ele_level3_1="//*[@id='kity_text_157']"

ele_level3_2="//*[@id='kity_text_165']"
ele_level4_1="//*[@id='kity_text_173']"
ele_level3_2_1="//*[@id='kity_text_181']"
ele_level3_2_2="//*[@id='kity_text_189']"


#各节点上数值显示元素定位 evaute

res_total='//*[@id="kity_text_393"]'

res_1='#kity_text_333'
res_2='#kity_text_357'
res_3='#kity_text_377'
res_4='#kity_text_385'
res_5='#kity_text_389'

res_1_1='#kity_text_321'
res_1_2='#kity_text_325'
res_1_3='#kity_text_329'

res_2_1='#kity_text_337'
res_2_2='#kity_text_341'
res_2_3='#kity_text_345'
res_2_4='#kity_text_349'
res_2_5='#kity_text_353'

res_3_1='#kity_text_361'
res_3_2='#kity_text_373'
res_3_2_1='#kity_text_365'
res_3_2_2='#kity_text_369'
res_4_1='#kity_text_381'


dict1={"final_total":'19.3',
        "final_1":'23.0',
        "final_2":'29.0',
        "final_3":'30.0',
        "final_4":'10.0',
        "final_5":'10',
        "final_1_1":'10',
        "final_1_2":'20',
        "final_1_3":'30',
        "final_2_1": '10',
        "final_2_2":'20',
        "final_2_3":'30',
        "final_2_4":'40',
        "final_2_5":'50',
        "final_3_1":'10',
        "final_3_2":'35.0',
        "final_3_2_1":'30',
        "final_3_2_2":'40',
        "final_4_1":'10'}




#####################################修改新增#############################################
#各节点上数值显示元素定位  modifyev

resm_total='//*[@id="kity_text_193"]'

resm_1='#kity_text_173'
resm_2='#kity_text_177'
resm_3='#kity_text_181'
resm_4='#kity_text_185'
resm_5='#kity_text_189'

resm_1_1='#kity_text_161'
resm_1_2='#kity_text_165'
resm_1_3='#kity_text_169'

dict2={"final_total":'6.75',
        "final_1":'23.0',
        "final_2":'1',
        "final_3":'1',
        "final_4":'1',
        "final_5":'10',
        "final_1_1":'10',
        "final_1_2":'20',
        "final_1_3":'30'
        }

# 赋值之后多有元素定位都重新定位
xpath1_3='//*[@id="kity_text_147"]'

#改完1_3后其它元素都重新定位
after_resm_total='//*[@id="kity_text_193"]'
after_resm_1='#kity_text_273'
after_resm_2='#kity_text_277'
after_resm_3='#kity_text_281'
after_resm_4='#kity_text_285'
after_resm_5='#kity_text_289'

after_resm_1_1='#kity_text_261'
after_resm_1_2='#kity_text_265'
after_resm_1_3='#kity_text_269'


###########################################################################子节点数值或权重为空#####################################################################
valueemptyqz1_3={"name":"分支1.3","qz":'',"sz":'30'}

empty_resm_1="#kity_text_73"

valueemptysz1_3={"name":"分支1.3","qz":'0.5',"sz":''}



############################################################################test_parempty_eva############################################################################

level1_1_ele="//*[@id='kity_text_89']"

level1_1_value={"name":"分支1.1","qz":'1',"sz":30}
level1_value={"name":"分支测试1","qz":'0.2',"sz":''}
level_total_value='//*[@id="kity_text_153"]'



####################################################################test_parempty_comf#####################################################################################

level1_value1={"name":"分支测试1","qz":'',"sz":'10'}


#################################################################test_modifycon############################################################################################

valueemptycon1_3={"name":"","qz":'0.5',"sz":'30'}
emptycon1_3={"name":"分支1.3—修改","qz":'0.5',"sz":'30'}



###############################################################test_modify_notsavw##########################################################################################

notsave_1_3={"name":"分支不保存1-3","qz":'3',"sz":'20'}



#######################################权重和小于和大于11的节点1.3值##############################


small_value1_3='0.4'
value1_3='0.6'
small_value1_2='0.4'



#######################################权重值为负数或者带字母#####################################
negative_value1_3='-0.5'
letter_value1_3='0.4aaa'





