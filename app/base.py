import subprocess
# from seting import Config
from settings import Config
from utils.helper import Params
import pickle
import os
import datetime


class BaseHandle(object):
    def __init__(self, device):
        self.device = device
        self.config = Params(Config().devices[device])
        self.id = self.config.id
        self.today = datetime.datetime.now().strftime("%Y-%m-%d")
        self.cache = self.config.cache_path
        self.app = Params(Config().app)

    def check_connect(self):
        try:
            subprocess.call("adb connect {}".format(self.id).split(), timeout=5)
        except Exception as e:
            print('add connect error {}'.format(str(e)))
            exit(1)

    def get_data(self):
        print("获取每日有效时长等app缓存数据")
        if not os.path.exists(self.cache):
            self.save_data()

        with open(self.cache, 'rb') as f:
            data = pickle.load(f)
            print("get data", data)

        return data

    def save_data(self, data=None):
        print("保存app缓存数据{}".format(data))
        data = {} if not data else data

        with open(self.cache, 'wb') as f:
            pickle.dump(data, f)

    def swipe(self, **kwargs):
        command = 'adb -s {0} shell input swipe {1} {2} {3} {4}'.format(self.id, *kwargs.get('xy'))
        return command

    def tap(self, **kwargs):
        command = "adb -s {0} shell input tap {1} {2}".format(self.id, *kwargs.get('xy'))
        return command

    def key_back(self):
        command = "adb -s {} shell input keyevent KEYCODE_BACK".format(self.id)
        return command

    def shell(self, **kwargs):
        kwargs = kwargs.get(self.device, kwargs)
        t = kwargs.get('type', None)
        print('{}: {}'.format(self.device, kwargs.get('desc', '')), kwargs.get('xy', kwargs.get('interval', '')))

        if t == 'swipe':
            command = self.swipe(**kwargs)

        elif t == 'tap':
            command = self.tap(**kwargs)

        elif t == 'sleep':
            command = 'sleep {}'.format(kwargs.get('interval'))

        else:
            command = kwargs.get('command')

        stats, rs = subprocess.getstatusoutput(command)
        if stats != 0:
            print('adb错误中断运行: {}'.format(rs))
            exit(-1)

        return stats, rs

    def light(self):
        """ 点亮屏幕 """
        self.shell(**{'command': 'adb -s {} shell input keyevent 26'.format(self.id)})
        self.shell(**{'command': 'adb -s {} shell input swipe  300 1233 300 617'.format(self.id)})

    def wtf(self):
        """ 获取包名 """
        command = 'adb -s {} shell am monitor'.format(self.id)
        # _, rs = self.shell(**{'command': command, 'desc': '获取包名'})
        print(command)
        self.shell(**{'command': self.key_back()})

    @staticmethod
    def hour():
        return datetime.datetime.now().hour


if __name__ == '__main__':
    a = BaseHandle('mix2s')
