import requests
import time
import datetime

now = int((time.time() + 3600 * 24) * 1000)

# url = "https://stock.xueqiu.com/v5/stock/quote.json?symbol=SZ300999&extend=detail"
# url3 = "https://stock.xueqiu.com/v5/stock/chart/kline.json?symbol=SH000001&begin={}&period=day&type=after&count=-1&indicator=kline,pe,pb,ps,pcf,market_capital,agt,ggt,balance".format(now)
# session = requests.Session()
# session.get(url="https://xueqiu.com", headers=headers)
# a = session.get(url=url, headers=headers).json()
# b = session.get(url=url2, headers=headers).json()
# c = session.get(url=url3, headers=headers).json()


class SZMarket(object):
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}

    def __init__(self):
        self.session = requests.Session()
        self.session.get(url="https://xueqiu.com", headers=SZMarket.headers)

    def detail(self, code, t="SH"):
        url = "https://stock.xueqiu.com/v5/stock/quote.json?symbol={}{}&extend=detail".format(t.upper(), code)
        rs = self.session.get(url=url, headers=SZMarket.headers).json()
        status = rs['data']['market']['status']
        quote = rs['data']['quote']
        t = quote['time']
        date = datetime.datetime.fromtimestamp(int(t / 1000))
        date_format = "{}-{}-{}".format(date.year, date.month, date.day)
        # 当前
        current = quote['current']
        print(rs)
        return {'status': status, 'date': date_format}


if __name__ == '__main__':
    a = SZMarket()
    a.detail('000001')


