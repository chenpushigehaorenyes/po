from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class More_page(BaseAction):
    gengduo=By.XPATH,"//*[@text='更多']"
    yidongwangluo = By.XPATH,"//*[@text='移动网络']"
    leixing = By.XPATH,"//*[@text='首选网络类型']"
    wangluo1  = By.XPATH,"//*[@text='2G']"
    wangluo2  = By.XPATH,"//*[@text='3G']"



    def gengduo_page(self):
        # self.driver.find_element_by_xpath("//*[@text='更多']").click()
        # self.find_element(self.gengduo).click()
        self.click(self.gengduo)
    def yidongwangluo_page(self):
        # self.driver.find_element_by_xpath("//*[@text='移动网络']").click()
        # self.find_element(self.yidongwangluo).click()
        self.click(self.yidongwangluo)

    def leixinf_page(self):
        # self.driver.find_element_by_xpath("//*[@text='首选网络类型']").click()
        self.find_element(self.leixing).click()
    def wangluo1_page(self):
        # self.driver.find_element_by_xpath("//*[@text='2G']").click()
        self.find_element(self.wangluo1).click()
    def wangluo2_page(self):
        # self.driver.find_element_by_xpath("//*[@text='3G']").click()
        self.find_element(self.wangluo2).click()
