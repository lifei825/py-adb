from .base import BaseHandle
import time


class Tomato(BaseHandle):
    def __init__(self, *args, **kwargs):
        super(Tomato, self).__init__(*args, **kwargs)
        self.action = self.app.tomato.action
        self.pkg = self.app.tomato.pkg

    def start(self):
        self.start_app()
        self.shell(**self.action.tap_sj)
        time.sleep(1)
        self.shell(**self.action.tap_book)

    def start_app(self):
        command = '''
                adb -s {0} shell am force-stop {1}
                sleep 2
                adb -s {0} shell monkey -p {1} 1
                '''.format(self.id, self.pkg)
        param = {'command': command}
        self.shell(**param)
        time.sleep(12)

    def sign_in(self):
        self.start_app()
        self.shell(**self.action.tap_fuli)
        time.sleep(3)
        for i in range(11):
            print(i+1)
            self.shell(**self.action.tap_ten_sp)
            self.shell(**self.action.wait_sp)
            self.shell(**self.action.tap_close_sp)
            time.sleep(1)

    def bx(self):
        print("领取番茄小说宝箱")
        self.start_app()
        time.sleep(5)
        self.shell(**self.action.tap_fuli)
        time.sleep(3)
        self.shell(**self.action.tap_bx)
        time.sleep(2)
        self.shell(**self.action.tap_bx_sp)
        self.shell(**self.action.wait_sp)
        self.shell(**self.action.tap_close_sp)

    def round(self, interval):
        print("看番茄小说, 等待{}s".format(interval))
        time.sleep(interval)
        self.shell(**self.action.tap_page)


class QQRead(Tomato):
    def __init__(self, *args, **kwargs):
        super(QQRead, self).__init__(*args, **kwargs)
        self.action = self.app.qqyd.action
        self.pkg = self.app.qqyd.pkg

    def start(self):
        self.start_app()
        self.shell(**self.action.tap_mf)
        time.sleep(1)
        self.shell(**self.action.tap_qyd)
        time.sleep(1)
        self.shell(**self.action.tap_book)

    def round(self, interval):
        print("QQ阅读, 等待{}s".format(interval))
        time.sleep(interval)
        self.shell(**self.action.tap_fy)
