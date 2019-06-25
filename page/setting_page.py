from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class Setting_page(BaseAction):
    display_button=By.XPATH,"//*[@text='显示']"
    gengduo=By.XPATH,"//*[@text='更多']"

    def click_display(self):
        self.click(self.display_button)

    def gengduo_page(self):
        self.click(self.gengduo)

