from .base import BaseHandle
import time


class TaoBao(BaseHandle):
    def __init__(self, *args, **kwargs):
        super(TaoBao, self).__init__(*args, **kwargs)
        self.action = self.app.tb.action
        self.pkg = self.app.tb.pkg

    def start(self):
        command = '''
        adb -s {0} shell am force-stop {1}
        sleep 2
        adb -s {0} shell monkey -p {1} 1
        '''.format(self.id, self.pkg)
        param = {'command': command}
        self.shell(**param)

    def round(self, interval):
        print("刷淘宝直播, 等待{}s".format(interval))
        self.shell(**self.action.tap_sp)
        self.shell(**self.action.swipe_sp)
        time.sleep(interval)


