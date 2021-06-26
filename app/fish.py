from .base import BaseHandle
import random
import time

fish_taps = {
    'mix2s': [
        (472, 831),
        (633, 625),
        (1428, 417),
        (1790, 719),
        (335, 867),
        (1735, 623),
        (1838, 406),
        (1111, 333),
    ],
    'redmi': [
        (1134, 431),
        (1333, 466),
        (674, 381),
        (459, 561),
        (944, 440),
        (1344, 575),
        (927, 143),
        (503, 186),
        (1569, 230)
    ],
    'huawei': [
        (472, 831),
        (453, 596),
        (1085, 831),
        (384, 781),
        (441, 531),
        (721, 545),
        (1527, 703),
        (1503, 826),
        (801, 670)
    ]
}


class Fish(BaseHandle):
    def __init__(self, *args, **kwargs):
        super(Fish, self).__init__(*args, **kwargs)
        self.action = self.app.fish.action

    def joke(self):
        print("兼职咸鱼搞笑赚")
        for i in range(5):
            time.sleep(12)
            self.shell(**self.action.tap_jiangli)
            time.sleep(5)
            self.shell(**self.action.tap_confirm_jiangli)
            self.shell(**self.action.tap_jiangli)

    def news(self):
        print("兼职咸鱼新闻赚")
        for i in range(5):
            self.shell(**self.action.tap_news)
            time.sleep(12)
            self.shell(**self.action.tap_back)
            time.sleep(6)
            self.shell(**self.action.tap_confirm_jiangli)
            # self.shell(**self.action.tap_back)

    def game_fish(self):
        print('开始捕鱼游戏')
        p = fish_taps[self.device]
        while 1:
            # action = {'desc': '发射鱼雷', 'xy': random.choice(p), 'type': 'tap'}
            action = {'desc': '发射鱼雷', 'xy': random.choice(p) + random.choice(p), 'type': 'swipe'}
            self.shell(**action)
            # time.sleep(1)


if __name__ == '__main__':
    aa = Fish()



