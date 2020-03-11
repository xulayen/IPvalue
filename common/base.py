from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from common.logger import *
logger=Logger(logger="method").getlog()
# exc_info = 1
class method():


    driver = webdriver.Chrome()



    def open(self):
        logger.info('打开浏览器...')
        self.url = "http://47.98.63.78:8088/#/"
        self.driver.get(self.url)
        self.driver.refresh()


    #定位元素
    def find_element(self,ele_attri,loc):
        try:

            #WebDriverWait(self.driver,6).until(ec.visibility_of_element_located(ele_attri,loc))
            WebDriverWait(self.driver, 6).until(lambda x: x.find_element(ele_attri,loc))
            return self.driver.find_element(ele_attri,loc)

        except Exception as e:
            logger.error('未找到元素%s',loc)




    def clear(self,ele_attri,loc):
        self.find_element(ele_attri,loc).clear()




    def sendkeys(self,ele_attri,loc,value):
        #self.clear(ele_attri,loc)
        self.find_element(ele_attri,loc).send_keys(value)

    def click(self,ele_attri,loc):
        self.find_element(ele_attri,loc).click()


    def  getvalue(self,ele_attri,loc,attribute):
        return self.find_element(ele_attri,loc).get_attribute(attribute)



    def contentclick(self,ele_attri,loc):
        elecomm=self.find_element(ele_attri,loc);
        ActionChains(self.driver).context_click(elecomm).perform()



    def maximize(self):
        self.driver.maximize_window()



    def ac_click(self,ele_attri,loc):
        self.elecomm=self.find_element(ele_attri,loc)
        ActionChains(self.driver).click(self.elecomm).perform()



    def quit(self):
        self.driver.quit()



    def close(self):
        self.driver.close()



        ###新增了git分支

