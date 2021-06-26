from .base import BaseHandle
import time


class DouYin(BaseHandle):
    def __init__(self, *args, **kwargs):
        super(DouYin, self).__init__(*args, **kwargs)
        self.action = self.app.douyin.action
        self.pkg = self.app.douyin.pkg

    def start(self):
        command = '''
        adb -s {0} shell am force-stop {2}
        sleep 2
        adb -s {0} shell am start {1}
        '''.format(self.id, self.pkg, self.pkg.split('/')[0])
        param = {'command': command}
        self.shell(**param)

    def sign_in(self):
        pass

    def bx(self):
        print("领取抖音宝箱")
        self.start()
        time.sleep(5)
        self.shell(**self.action.tap_gold)
        time.sleep(5)
        self.shell(**self.action.tap_bx)
        time.sleep(2)
        self.shell(**self.action.tap_bx_sp)
        self.shell(**self.action.wait_sp)
        self.shell(**{'command': self.key_back()})
        time.sleep(1)
        self.shell(**self.action.close_sp)
        time.sleep(2)
        self.shell(**self.action.tap_xs_sp)
        self.shell(**self.action.wait_sp)
        self.shell(**{'command': self.key_back()})
        time.sleep(1)
        self.shell(**self.action.close_sp)

    def round(self, interval):
        print("刷抖音视频, 等待{}s".format(interval))
        time.sleep(interval)
        self.shell(**self.action.swipe_sp)



