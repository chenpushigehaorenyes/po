import time

from appium import webdriver
class Test_setting:
    def setup(self):
        desired_caps = dict()
        # 手机参数
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        # 应用参数
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.Settings'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
    def teardown(self):
        time.sleep(2)
        self.driver.quit()
    # 获取driver
    def test_2g(self):
        self.driver.find_element_by_xpath("//*[@text='更多']").click()
        self.driver.find_element_by_xpath("//*[@text='移动网络']").click()
        self.driver.find_element_by_xpath("//*[@text='首选网络类型']").click()
        self.driver.find_element_by_xpath("//*[@text='2G']").click()

    def test_3g(self):
        self.driver.find_element_by_xpath("//*[@text='更多']").click()
        self.driver.find_element_by_xpath("//*[@text='移动网络']").click()
        self.driver.find_element_by_xpath("//*[@text='首选网络类型']").click()
        self.driver.find_element_by_xpath("//*[@text='3G']").click()

    def test_hello(self):
        self.driver.find_element_by_xpath("//*[@text='显示']").click()
        self.driver.find_element_by_xpath("//*[@content-desc='搜索']").click()
        self.driver.find_element_by_id("android:id/search_src_text").send_keys("hello")
        self.driver.find_element_by_xpath("//*[@content-desc='收起']").click()




