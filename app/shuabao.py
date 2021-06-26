from .base import BaseHandle
import time


class ShuaBao(BaseHandle):
    def __init__(self, *args, **kwargs):
        super(ShuaBao, self).__init__(*args, **kwargs)
        self.action = self.app.shuabao.action
        self.pkg = self.app.shuabao.pkg

    def start(self):
        command = '''
                adb -s {0} shell am force-stop {1}
                sleep 2
                adb -s {0} shell monkey -p {1} 1
                '''.format(self.id, self.pkg)
        param = {'command': command}
        self.shell(**param)

        if self.device == 'redmi':
            time.sleep(15)
            self.shell(**{'desc': "点击推荐", 'xy': (494, 124), 'type': 'tap'})

    def sign_in(self):
        self.start()
        time.sleep(15)
        self.shell(**self.action.tap_task)
        time.sleep(3)
        self.shell(**self.action.tap_close_pop)
        time.sleep(2)
        self.shell(**self.action.tap_sign)
        time.sleep(2)
        self.shell(**self.action.tap_sign_sp)
        self.shell(**self.action.wait_sp)
        self.shell(**self.action.tap_close_sp)
        time.sleep(2)
        self.shell(**self.action.tap_close_pop)

    def round(self, interval):
        print("刷刷宝视频, 等待{}s".format(interval))
        time.sleep(interval)
        self.shell(**self.action.swipe_sp)


