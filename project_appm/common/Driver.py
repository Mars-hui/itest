#coding = utf - 8
from appium import webdriver
import time

class Driver(object):
    def startUp(self):
        print("启动appium")
        desired_caps = {
            "deviceName": "127.0.0.1:21503",
            "platformName": "Android",
            "platformVersion": "5.1.1",
            "appPackage": "com.ss.android.article.news",
            "appActivity": "com.ss.android.article.news.activity.MainActivity",
            "noReset": True,
            "unicodeKeyboard": True
        }
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        time.sleep(6)
        return driver
# if __name__ == '__main__':
#     appm = Driver()
#     driver = appm.startUp()
#     driver.find_element_by_id("com.ss.android.article.news:id/bov").click()

