#coding = utf-8
import unittest
from common.Driver import Driver
from common.MyTest import MyTest
import time
from common.public import Public

class HomeTest(MyTest):
    def test_weitoutiao(self):
        self.driver.find_element_by_id("com.ss.android.article.news:id/bov").click()
        #点击发微头条
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView').click()
        #点击分享新鲜事，并输入内容
        self.driver.find_element_by_id('com.ss.android.article.news:id/blh').send_keys('今天是个大晴天')
        #点击‘发布’按钮
        self.driver.find_element_by_id('com.ss.android.article.news:id/a8n').click()
        time.sleep(2)

    #刷新首页
    # def test2(self):
    #     # x = self.driver.get_window_size()['width']
    #     # y = self.driver.get_window_size()['height']
    #     # x1 = int(x * 0.5)
    #     # y1 = int(y * 0.5)
    #     # y2 = int(y * 0.8)
    #     # t= 1000
    #     # self.driver.swipe(x1, y1, x1, y2, t)
    #     # time.sleep(6)
    #
    #     p = Public()
    #     p.swipDown(self.driver)
    #     time.sleep(6)



if __name__ == '__main__':
    unittest.main()





'''【总结】
HomeTest 继承MyTest，而MyTest继承unitest，
所以HomeTest依然是用unitest框架，自动执行MyTest中的setUp()\tearDown()

'''