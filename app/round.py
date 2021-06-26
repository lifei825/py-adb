from .base import BaseHandle
from .toutiao import TouTiao
from .kuaishou import KuaiShou
from .tomato import Tomato, QQRead
from .douyin import DouYin
from .shuabao import ShuaBao
from .weishi import WeiShi
from .qutt import QuTT
from .taobao import TaoBao
from .huoshan import HuoShan
from .clear import Clear
from .kuaiKanDian import KuaiKanDian
import random


class RoundBx(Clear):
    def __init__(self, *args, **kwargs):
        super(RoundBx, self).__init__(*args, **kwargs)
        self.limit = 3600 * 3

    def sign_in(self):
        pass

    def round_all(self, task='round_all'):
        round_list = []
        print("大任务循环", task)
        tt = TouTiao(self.device)

        ks = KuaiShou(self.device)
        fq = Tomato(self.device)
        dy = DouYin(self.device)
        # sb = ShuaBao(self.device)
        qtt = QuTT(self.device)
        hs = HuoShan(self.device)
        tb = TaoBao(self.device)
        kkd = KuaiKanDian(self.device)

        if self.device == 'huawei':
            round_list = [
                ('tb_second', tb, 0.5 * 3600),
                ('kkd_second', kkd, 0.5 * 3600),
                ('ks_second', ks, 0.5 * 3600),
                ('fq_second', fq, 0.5 * 3600),
                ('dy_second', dy, 0.5 * 3600),
                # ('sb_second', sb, 1.8 * 3600),
                # ('qtt_second', qtt, 2 * 3600),
                # ('hs_second', hs, 1.5 * 3600),
            ]
        if self.device == 'mix2s':
            ws = WeiShi(self.device)
            qq = QQRead(self.device)
            round_list = [
                # ('qq_second', qq, 1 * 3600),
                ('tb_second', tb, 0.5 * 3600),
                ('kkd_second', kkd, 0.5 * 3600),
                # ('sb_second', sb, 1.5 * 3600),
                ('ws_second', ws, 0.5 * 3600),
                ('ks_second', ks, 0.5 * 3600),
                ('dy_second', dy, 0.5 * 3600),
                ('fq_second', fq, 0.5 * 3600),
                # ('qtt_second', qtt, 1 * 3600),
                # ('hs_second', hs, 1 * 3600),
            ]

        if self.device == 'redmi':
            round_list = [
                ('tb_second', tb, 0.5 * 3600),
                ('kkd_second', kkd, 0.5 * 3600),
                ('ks_second', ks, 0.5 * 3600),
                # ('sb_second', sb, 1.5 * 3600),
                ('qtt_second', qtt, 0.5 * 3600),
                ('dy_second', dy, 0.5 * 3600),
                # ('hs_second', hs, 2 * 3600),
            ]

        tt_bx, dy_bx, fq_bx, qtt_bx, qtt_egg, ks_bx, hs_bx = 0, 0, 0, 0, 0, 0, 0
        for name, app, limit_second in round_list:
            # 获取当天数据并累加保存,覆盖之前的数据
            data = self.get_data().get(self.today, {})

            sum_second = data.get(name, 0)

            if sum_second < limit_second:
                app.start()

            while sum_second < limit_second:
                interval = random.randint(8, 16) if name != 'jd_second' else random.randint(7, 9)
                app.round(interval)
                if tt_bx > 10 * 60 and self.device not in ['emt']:
                    tt.bx()
                    tt_bx = 0
                    app.start()

                if dy_bx > 60 * 21:
                    dy.bx()
                    dy_bx = 0
                    app.start()

                if fq_bx > 60 * 20 and self.device not in ['redmi']:
                    fq.bx()
                    fq_bx = 0
                    app.start()

                if qtt_bx > 60 * 60 and self.device in ['mix2s', 'redmi', 'huawei']:
                    qtt.bx()
                    qtt_bx = 0
                    app.start()
                    if self.device == 'huawei':
                        self.clear()

                if name == 'qtt_second' and qtt_egg > 5 * 60 and self.device in ['mix2s']:
                    qtt.egg()
                    qtt_egg = 0
                    app.start()

                if ks_bx > 60 * 59:
                    ks.bx()
                    ks_bx = 0
                    app.start()

                # if hs_bx > 60 * 22:
                #     hs.bx()
                #     hs_bx = 0
                #     app.start()

                tt_bx += interval
                dy_bx += interval
                fq_bx += interval
                qtt_bx += interval
                ks_bx += interval
                hs_bx += interval
                if name == 'qtt_second':
                    qtt_egg += interval
                print('tt cd {}, dy cd {}, fq cd {}, qtt bx cd {}, qtt egg cd {}, ks bx cd {}'.format(
                    tt_bx, dy_bx, fq_bx, qtt_bx, qtt_egg, ks_bx))
                print('hs cd {}'.format(hs_bx))

                if name == 'jd_second':
                    data = self.get_data().get(self.today, {})

                sum_second += interval
                data[name] = sum_second

                # 睡眠奖励 0我要睡了 1我睡醒了 2睡眠中或等待睡眠
                # if 24 > self.hour() >= 20:
                #     if data.get('tt_sleep', 0) != 2 and self.device != 'mix2s':
                #         data['tt_sleep'] = 2
                #         tt.start_sleep()
                #         app.start()
                #
                # if 19 > self.hour() >= 8:
                #     if data.get('tt_sleep',s0) != 1 and self.device != 'mix2s':
                #         data['tt_sleep'] = 1
                #         tt.start_sleep(1)
                #         app.start()

                # if data.get('qtt_sign', 0) != 1 and self.device in ['huawei']:
                #     data['qtt_sign'] = 1
                #     qtt.sign_in()
                #     app.start()

                # if data.get('sb_sign', 0) != 1:
                #     data['sb_sign'] = 1
                #     sb.sign_in()
                #     app.start()

                self.save_data({self.today: data})




