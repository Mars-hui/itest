#coding=utf-8
from appium import webdriver
import time

def startUp():
    print('启动app')

    desired_caps = {
        "deviceName": "127.0.0.1:21503",
        "platformName": "Android",
        "platformVersion": "5.1.1",
        "appPackage": "com.ss.android.article.news",
        "appActivity": "com.ss.android.article.news.activity.MainActivity",
        "noReset": True,
        "unicodeKeyboard": True
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
    # driver = webdriver.Remote('http://192.168.1.20:4723/wd/hub',desired_caps)
    driver.find_element_by_id('com.ss.android.article.news:id/bov').click()
    time.sleep(1)
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView').click()
    time.sleep(1)
    # driver.find_element_by_text('分享新鲜事').send_keys('appium测试')
    driver.find_element_by_android_uiautomator('分享新鲜事').send_keys('appium测试')
    time.sleep(1)
    driver.find_element_by_class_name('android.widget.TextView').click()

    #用Xpath定位

    driver.find_element_by_xpath('//*[@id="com.ss.android.article.news:id/cju"]').click()




    print('已经启动，等待6s...')
startUp()