from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class Display_page(BaseAction):

    display_button=By.XPATH,"//*[@text='显示']"
    search_button=By.XPATH,"//*[@content-desc='搜索']"
    search_edit_text=By.XPATH,"//*[@text='搜索…']"
    back_button = By.XPATH,"//*[@content-desc='收起']"

    def click_display(self):
        # self.driver.find_element_by_xpath("//*[@text='显示']").click()
        # self.find_element(self.display_button).click()
        self.click(self.display_button)

    def click_search(self):
        # self.driver.find_element_by_xpath("//*[@content-desc='搜索']").click()
        # self.find_element(self.search_button).click()
        self.click(self.search_button)

    def input_serach(self,content):
        # self.driver.find_element_by_id("android:id/search_src_text").send_keys("hello")
        # self.driver.find_element_by_xpath("//*[@text='搜索…']").send_keys("hello")
        # self.find_element(self.search_edit_text).send_keys("hello")
        self.input(self.search_edit_text,content)
    def click_back(self):
        # self.driver.find_element_by_xpath("//*[@content-desc='收起']").click()
        # self.find_element(self.back_button).click()
        self.click(self.back_button)
