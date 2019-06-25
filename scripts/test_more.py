import os,sys

from page.page import Page

sys.path.append(os.getcwd())
import time

from appium import webdriver

from base.base_driver import init_driver
from page.more_page import More_page

class Test_more:
    def setup(self):
        # base

        self.driver = init_driver()
        # page
        self.page =Page(self.driver)
        # self.more_page1 = More_page(self.driver)
    def teardown(self):
        time.sleep(2)
        self.driver.quit()
    # 获取driver
    def test_2g(self):
        self.page.setting.gengduo_page()
        self.page.Morepage.yidongwangluo_page()
        self.page.MobileNetwork_Page.leixinf_page()
        self.page.MobileNetwork_Page.wangluo1_page()



    def test_3g(self):
        self.page.setting.gengduo_page()
        self.page.Morepage.yidongwangluo_page()
        self.page.MobileNetwork_Page.leixinf_page()
        self.page.MobileNetwork_Page.wangluo2_page()


