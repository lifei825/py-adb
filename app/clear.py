from .base import BaseHandle
import time


class Clear(BaseHandle):
    def __init__(self, *args, **kwargs):
        super(Clear, self).__init__(*args, **kwargs)
        self.action = self.app.clears.action
        self.pkg = self.app.clears.pkg

    def start(self):
        command = '''
        adb -s {0} shell am force-stop {1}
        sleep 2
        adb -s {0} shell monkey -p {1} 1
        '''.format(self.id, self.pkg)
        param = {'command': command}
        self.shell(**param)

    def clear(self):
        print("清理缓存")
        self.start()
        time.sleep(2)
        self.shell(**self.action.tap_qljs)
        self.shell(**self.action.wait_sm)
        self.shell(**self.action.tap_yjql)
        time.sleep(5)


