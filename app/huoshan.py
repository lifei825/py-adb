from .base import BaseHandle
import time


class HuoShan(BaseHandle):
    def __init__(self, *args, **kwargs):
        super(HuoShan, self).__init__(*args, **kwargs)
        self.action = self.app.huoshan.action
        self.pkg = self.app.huoshan.pkg

    def start(self):
        command = '''
        adb -s {0} shell am force-stop {1}
        sleep 2
        adb -s {0} shell monkey -p {1} 1
        '''.format(self.id, self.pkg)
        param = {'command': command}
        self.shell(**param)

    def sign_in(self):
        pass

    def bx(self):
        print("领取火山宝箱")
        self.start()
        time.sleep(6)
        self.shell(**self.action.tap_gold)
        time.sleep(5)
        self.shell(**self.action.tap_bx)
        time.sleep(2)
        self.shell(**self.action.tap_bx_sp)
        self.shell(**self.action.wait_sp)
        self.shell(**self.action.close_sp)

    def round(self, interval):
        print("刷火山视频, 等待{}s".format(interval))
        time.sleep(interval)
        self.shell(**self.action.swipe_sp)



