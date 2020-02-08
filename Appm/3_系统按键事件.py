#coding = utf - 8
from appium import webdriver

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
#点home键
# driver.press_keycode(3)
# #重置app
# driver.reset()
# #启动app的某一个activity:start_activity(包名,activity名)
# driver.start_activity("com.wuba.zhuanzhuan","./presentation.view.activity.LaunchActivity")
#获得所有contexts
driver.contexts
# #current_context:查看当前的context
# driver.current_context
# #切换context:switch_to.context(context名)
# driver.switch_to.context("")

