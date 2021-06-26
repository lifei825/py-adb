import click
from seting import Config
from app.fish import Fish
from app.toutiao import TouTiao
from app.kuaishou import KuaiShou
from app.douyin import DouYin
from app.round import RoundBx
from app.tomato import Tomato
from app.shuabao import ShuaBao
from app.qutt import QuTT
from app.huoshan import HuoShan
from app.clear import Clear
import time
import datetime


@click.command()
@click.option('-d', '--device', type=click.Choice(Config.devices.keys()), help="指定手机设备")
@click.option('-t', '--task', default='round_all', help='指定任务')
def run(device, task):
    click.echo("start device: {}".format(device))

    app_type = task.split('_')[0]
    if app_type == 'ks':
        app = KuaiShou(device)
    elif app_type == 'fish':
        app = Fish(device)
    elif app_type == 'tt':
        app = TouTiao(device)
    elif app_type == 'dy':
        app = DouYin(device)
    elif app_type == 'fq':
        app = Tomato(device)
    elif app_type == 'sb':
        app = ShuaBao(device)
    elif app_type == 'qtt':
        app = QuTT(device)
    elif app_type == 'hs':
        app = HuoShan(device)
    else:
        app = RoundBx(device)

    # check adb connect
    if device in ['mix2s']:
        app.check_connect()

    if task == 'ks_sp_ten':
        app.sp_ten()

    elif task == 'ks_zb_ten':
        app.zb_ten()

    elif task in ['tt_bx', 'dy_bx', 'fq_bx', 'qtt_bx', 'ks_bx', 'hs_bx']:
        app.bx()

    elif task in ['sb_sign', 'qtt_sign', 'fq_sign']:
        app.sign_in()

    elif task == 'fish_joke':
        app.joke()

    elif task == 'fish_news':
        app.news()

    elif task == 'fish_game':
        app.game_fish()

    elif task == 'qtt_egg':
        app.egg()

    elif task == 'light':
        app.light()

    elif task == 'wtf':
        app.wtf()

    elif task == 'clear':
        app = Clear(device)
        app.clear()

    else:
        n = 0
        while 1:
            # app.light()
            try:
                print("today:", app.today)
                app.round_all(task)
            except Exception as e:
                print('err', str(e))

            if device == 'mix2s222':
                time.sleep(3600 * 3)
            else:
                time.sleep(10)
                n += 1
                app.today = datetime.datetime.now().strftime("%Y-%m-%d")
                app.save_data({app.today+"-"+str(n): {}})


if __name__ == '__main__':
    run()
