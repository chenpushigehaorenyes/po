from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SearchPage(BaseAction):
    search_edit_text = By.XPATH, "//*[@text='搜索…']"
    back_button = By.XPATH, "//*[@content-desc='收起']"
    def input_serach(self,content):
        self.input(self.search_edit_text,content)
    def click_back(self):
        self.click(self.back_button)
