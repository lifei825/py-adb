from wxDB.db import CloudDb
from xueQ.sz import SZMarket
import os
import random
import time
from functools import wraps
import datetime

db = CloudDb(config='{}/wxDB/config.pk'.format(os.getcwd()))
market = SZMarket()
hmd = []


# 装饰器函数失败重试, n失败重试次数， s失败等待时间
def fail_retry(n=3, s=3):
    def retry_decorator(func):
        @wraps(func)
        def wrap_function(*args, **kwargs):
            for i in range(n):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print("err retry {}: {}".format(i+1, str(e)))
                    time.sleep(s)
        return wrap_function
    return retry_decorator


def today():
    now = datetime.datetime.now()
    return '{}-{}-{}'.format(now.year, now.month, now.day)


def is_open():
    """ 开盘日排除分时休盘范围 """
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    if hour == 11 and minute < 30:
        return True

    elif hour == 9 and minute > 29:
        return True

    elif hour in [10, 13, 14]:
        return True

    else:
        return False


@fail_retry()
def update_market():
    sh = market.detail('000001')
    sz = market.detail('399001', 'sz')
    date = sh.get('date', '')
    print("date", date)
    if date == today():
        db.update_market(sh, sz)
    else:
        # 当天日期对不上则加入黑名单，如果是当天开盘还要进一步判断是否在开盘时间范围内
        hmd.append(date)


@fail_retry()
def once_market():
    sh = market.detail('000001')
    sz = market.detail('399001', 'sz')
    date = sh.get('date', '')
    # 查询有今天股市信息吗，没有则补录
    rs = db.search_market(date)
    if rs.get("pager").get("Total") == 0:
        db.update_market(sh, sz)
    exit(0)


if __name__ == '__main__':
    # 当天忘了保存，可运行次方法
    # once_market()

    while True:
        state = is_open()
        if today() not in hmd:
            if state:
                update_market()
            else:
                print("休市中...")

        else:
            print("今天不开盘")

        # 每隔5-12秒抓一次数据存入数据库，小程序端每15秒从数据库读取
        time.sleep(random.randint(5, 12))

