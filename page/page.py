from page.display_page import Display_page
from page.mobile_network_page import MobileNetworkPage
from page.more_page import More_page
from page.search_page import SearchPage
from page.setting_page import Setting_page


class Page:
    def __init__(self,driver):
        self.driver = driver

    @property
    def setting(self):
        return  Setting_page(self.driver)

    @property
    def dispiay_page(self):
        return Display_page(self.driver)

    @property
    def search(self):
        return SearchPage(self.driver)

    @property
    def MobileNetwork_Page(self):
        return MobileNetworkPage(self.driver)

    @property
    def Morepage(self):
        return More_page(self.driver)
