from .base import BaseHandle
import time


class TouTiao(BaseHandle):
    def __init__(self, *args, **kwargs):
        super(TouTiao, self).__init__(*args, **kwargs)
        self.action = self.app.toutiao.action
        self.pkg = self.app.toutiao.pkg

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
        print("领取头条宝箱")
        self.start()
        time.sleep(10)
        self.shell(**self.action.tap_task)
        time.sleep(5)
        self.shell(**self.action.tap_bx)
        time.sleep(3)
        self.shell(**self.action.tap_bx_sp)
        self.shell(**self.action.wait_sp)
        self.shell(**self.action.close_sp)
        time.sleep(1)
        self.shell(**self.action.close_sp)

    def start_sleep(self, stat=2):
        print('我要睡了')
        self.start()
        time.sleep(15)
        self.shell(**self.action.tap_task)
        time.sleep(2)
        self.shell(**self.action.tap_sleep)
        time.sleep(2)
        self.shell(**self.action.tap_sleep_start)
        if stat == 1:
            time.sleep(2)
            self.shell(**self.action.tap_sleep_start)

        time.sleep(2)



