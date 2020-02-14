#coding = utf - 8
from common import Driver
#发微头条

#点击发布按钮
class Test1(object):
    driver = Driver.getDriver()
    def sendMes(self,driver):
        driver.find_element_by_id("com.ss.android.article.news:id/bov").click()
        #点击发微头条
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView').click()
        #点击分享新鲜事，并输入内容
        driver.find_element_by_id('com.ss.android.article.news:id/blh').send_keys('今天是个大晴天')
        #点击‘发布’按钮
        driver.find_element_by_id('com.ss.android.article.news:id/a8n').click()

if __name__ == '__main__':
    appm = Driver()
    driver = appm.startUp()
    t = Test1()
    Test1.sendMes(driver)