#coding=utf-8
#头条登录并发帖
from appium import webdriver
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import time


print("启动appium")
desired_caps={
    "deviceName": "127.0.0.1:21503",
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "appPackage": "com.ss.android.article.news",
    "appActivity": "com.ss.android.article.news.activity.MainActivity",
    "noReset": True,
    "unicodeKeyboard": True

}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
def start_appm():
    time.sleep(6)
    # #点击发布按钮
    # driver.find_element_by_id("com.ss.android.article.news:id/bov").click()
    # #点击发微头条
    # driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView').click()
    # #点击分享新鲜事，并输入内容
    # driver.find_element_by_id('com.ss.android.article.news:id/blh').send_keys('今天是个大晴天')
    # #点击‘发布’按钮
    # driver.find_element_by_id('com.ss.android.article.news:id/a8n').click()

    #使用text定位
    driver.find_elements_by_android_uiautomator('new UiSelector().text("我的")')[0].click()
    #使用另一种定位方法find_element(By.ID,'')
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.FrameLayout[3]/android.widget.TabWidget/android.widget.RelativeLayout[1]/android.widget.ImageView').click()
#1.driver.tap([坐标]，持续点击时间)
    driver.tap([18,338],1)
#2.TouchAction(driver)
    # *短按(press)
    # *释放(release)
    # *移动到(moveTo)
    # *点击(tap)
    # *等待(wait)
    # *长按(longPress)
    # *取消(cancel)
    # *执行(perform)
    action = TouchAction(driver)
    action.tap(driver.find_element_by_id('')).press().release().perform()
    #一个多次滑屏的例子：
    action.press(x=220, y=700).move_to(x=840, y=700).move_to(x=220, y=1530).release().perform()
#3.MultiAction()//多点触控
    action0 = TouchAction().tap('')
    action1 = TouchAction().tap('')
    MultiAction().add(action0).add(action1).perform()

#4.  滑动driver.swipe(x1, y1, x2, y2,duration)
    #可以通过【driver.get_window_size()】命令获得窗口高和宽
#获得屏幕大小宽和高
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['heigh']
    return (x,y)
#屏幕向上滑动
def swipeUp(t=1000):
    l = getSize()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.75)
    y2 = int(l[1] * 0.25)
    driver.swipe(x1, y1, x1, y2, t)
#屏幕向左滑动
def swipLeft(t):
    l = getSize()
    x1 = int(l[0] * 0.75)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.05)
    driver.swipe(x1, y1, x1, x2, t)
    













start_appm()