from .base import BaseHandle
import time


class QuTT(BaseHandle):
    def __init__(self, *args, **kwargs):
        super(QuTT, self).__init__(*args, **kwargs)
        self.action = self.app.qutt.action
        self.pkg = self.app.qutt.pkg

    def start_app(self):
        command = '''
        adb -s {0} shell am force-stop {1}
        sleep 2
        adb -s {0} shell monkey -p {1} 1
        sleep 13
        '''.format(self.id, self.pkg)
        param = {'command': command}
        self.shell(**param)

    def start(self):
        self.start_app()
        self.shell(**self.action.tap_xsp)

    def sign_in(self):
        self.start_app()
        self.shell(**self.action.tap_task)
        time.sleep(3)
        # self.shell(**self.action.tap_sign)
        # self.shell(**self.action.wait_sp)
        # self.shell(**self.action.tap_sign_close)
        # self.shell(**self.action.tap_tree)
        # time.sleep(2)
        # self.shell(**self.action.tap_tree_gold)
        # self.shell(**self.action.wait_sp)

    def bx(self):
        self.start_app()
        self.shell(**self.action.tap_tt)
        time.sleep(2)
        self.shell(**self.action.tap_bx)
        time.sleep(2)

    def egg(self):
        self.start_app()
        self.shell(**self.action.tap_xsp)
        time.sleep(5)
        self.shell(**self.action.tap_xsp_egg)
        time.sleep(2)

    def round(self, interval):
        print("刷趣头条, 等待{}s".format(interval))
        time.sleep(interval)
        self.shell(**self.action.swipe_sp)


