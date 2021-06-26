from .base import BaseHandle
import time


class WeiShi(BaseHandle):
    def __init__(self, *args, **kwargs):
        super(WeiShi, self).__init__(*args, **kwargs)
        self.action = self.app.weishi.action
        self.pkg = self.app.weishi.pkg

    def start(self):
        command = '''
        adb -s {0} shell am force-stop {1}
        sleep 2
        adb -s {0} shell monkey -p {1} 1
        '''.format(self.id, self.pkg)
        param = {'command': command}
        self.shell(**param)

    def round(self, interval):
        print("刷微视视频, 等待{}s".format(interval))
        time.sleep(interval)
        self.shell(**self.action.swipe_sp)


