from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MobileNetworkPage(BaseAction):

    # 首选网络类型 按钮
    leixing = By.XPATH, "//*[@text='首选网络类型']"



    # 2g 按钮
    wangluo1 = By.XPATH, "//*[@text='2G']"

    # 3g 按钮
    wangluo2 = By.XPATH, "//*[@text='3G']"

    # 点击 首选网络类型
    def leixinf_page(self):
        # self.driver.find_element_by_xpath("//*[@text='首选网络类型']").click()
        self.find_element(self.leixing).click()

    # 点击 2G
    def wangluo1_page(self):
        # self.driver.find_element_by_xpath("//*[@text='2G']").click()
        self.find_element(self.wangluo1).click()

    def wangluo2_page(self):
        # self.driver.find_element_by_xpath("//*[@text='3G']").click()
        self.find_element(self.wangluo2).click()
