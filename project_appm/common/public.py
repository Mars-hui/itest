#coding = utf -8

class Public(object):

    #获得屏幕尺寸
    def getSize(self,driver):
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        return (x, y)

    # 向下滑动
    def swipDown(self,driver,t=1000):
        l = self.getSize(driver)
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.5)
        y2 = int(l[1] * 0.8)
        driver.swipe(x1, y1, x1, y2, t)
