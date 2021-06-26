from .base import BaseHandle
import time


class KuaiKanDian(BaseHandle):
    def __init__(self, *args, **kwargs):
        super(KuaiKanDian, self).__init__(*args, **kwargs)
        self.action = self.app.kkd.action
        self.pkg = self.app.kkd.pkg

    def start(self):
        command = '''
        adb -s {0} shell am force-stop {1}
        sleep 2
        adb -s {0} shell monkey -p {1} 1
        sleep 10
        '''.format(self.id, self.pkg)
        param = {'command': command}
        self.shell(**param)

    def round(self, interval):
        print("刷快看点小视频, 等待{}s".format(interval))
        self.shell(**self.action.tap_sp)
        time.sleep(1)
        self.shell(**self.action.swipe_sp)
        time.sleep(interval)


