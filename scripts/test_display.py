import os,sys

from page.page import Page

sys.path.append(os.getcwd())

import time

from appium import webdriver

from base.base_driver import init_driver
from page.display_page import Display_page


class Test_display:


    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()
    def test_hello(self):
        self.page.setting.click_display()
        self.page.dispiay_page.click_search()
        self.page.search.input_serach("hello")
        self.page.search.click_back()


        # self.driver.find_element_by_xpath("//*[@text='显示']").click()
        # self.driver.find_element_by_xpath("//*[@content-desc='搜索']").click()
        # # self.driver.find_element_by_id("android:id/search_src_text").send_keys("hello")
        # self.driver.find_element_by_xpath("//*[@text='搜索…']").send_keys("hello")
        #
        # self.driver.find_element_by_xpath("//*[@content-desc='收起']").click()
