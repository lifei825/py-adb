import requests

url = "https://stock.xueqiu.com/v5/stock/quote.json?symbol=SZ300999&extend=detail"
url2 = "https://stock.xueqiu.com/v5/stock/quote.json?symbol=SH000001&extend=detail"
url3 = "https://stock.xueqiu.com/v5/stock/chart/kline.json?symbol=SH000001&begin=1647243479694&period=day&type=after&count=-5&indicator=kline,pe,pb,ps,pcf,market_capital,agt,ggt,balance"
headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
session = requests.Session()
session.get(url="https://xueqiu.com", headers=headers)
a = session.get(url=url, headers=headers).json()
b = session.get(url=url2, headers=headers).json()
c = session.get(url=url3, headers=headers).json()

if __name__ == '__main__':
    print(a)
    print(b)
    print(c)
