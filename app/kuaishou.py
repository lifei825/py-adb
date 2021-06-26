from .base import BaseHandle
import time


class KuaiShou(BaseHandle):
    def __init__(self, *args, **kwargs):
        super(KuaiShou, self).__init__(*args, **kwargs)
        self.action = self.app.kuaishou.action
        self.pkg = self.app.kuaishou.pkg

    def start(self):
        command = '''
        adb -s {0} shell am force-stop {1}
        sleep 2
        adb -s {0} shell monkey -p {1} 1
        sleep 3
        adb -s {0} shell input keyevent KEYCODE_BACK
        '''.format(self.id, self.pkg)
        param = {'command': command}
        self.shell(**param)

    def sign_in(self):
        pass

    def sp_ten(self):
        print("开始任务：快手每天10次广告视频")
        # self.start()
        # time.sleep(5)
        # self.shell(**self.action.tap_menu)
        # time.sleep(2)
        # self.shell(**self.action.tap_menu_money)

        # self.shell(**self.action.tap_hb)
        # time.sleep(10)
        # if self.device == 'huawei':
        #     self.shell(**self.action.swipe_sp)
        for i in range(11):
            print(i+1)
            time.sleep(3)
            self.shell(**self.action.tap_fuli)
            self.shell(**self.action.wait_sp)
            self.shell(**self.action.tap_close_sp)

    def zb_ten(self):
        print("10次每16秒直播得100金币")
        # self.start()
        # time.sleep(5)
        # self.shell(**self.action.tap_menu)
        # time.sleep(2)
        # self.shell(**self.action.tap_menu_money)
        # time.sleep(10)
        # self.shell(**self.action.swipe_sp)
        # time.sleep(1)
        # self.shell(**self.action.tap_zb)
        # time.sleep(5)
        for i in range(15):
            print(i+1)
            time.sleep(32)
            self.shell(**self.action.swipe_sp)

    def round(self, interval):
        print("刷快手视频, 等待{}s".format(interval))
        time.sleep(interval)
        self.shell(**self.action.swipe_sp)

    def bx(self):
        print('快手宝箱')
        self.start()
        time.sleep(5)
        # self.shell(**self.action.tap_menu)
        # time.sleep(2)
        # self.shell(**self.action.tap_menu_money)
        self.shell(**self.action.tap_hb)
        time.sleep(10)
        self.shell(**self.action.tap_bx)






