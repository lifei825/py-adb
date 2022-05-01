import requests
import json


class CloudDb(object):
    def __init__(self):
        print(123)
        conf = open('config.pk')
        appid, secret, env = [i[:-1] for i in conf.readlines()]
        self.url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'.format(appid, secret)
        self.tk = self.token()
        self.env = env

    def token(self):
        rs = requests.get(self.url).json()
        print('ttt', rs)
        return rs

    def add(self):
        url = 'https://api.weixin.qq.com/tcb/databaseadd?access_token={}'.format(self.tk.get('access_token', ''))
        print(url)
        d = {'data': [
            {'active': 'true', 'day': 2, 'month': 4, 'year': 2021, 'bottomInfo': "美3月非农就业", 'topInfo': '美港休市',
             'news': [{'desc': '美国3月非农就业数据', 'level': 1}]},
            {'active': 'true', 'day': 5, 'month': 4, 'year': 2021, 'bottomInfo': "清明节翌日", 'topInfo': 'A港休市'},
            {'active': 'true', 'day': 6, 'month': 4, 'year': 2021, 'bottomInfo': "复活节翌日", 'topInfo': '港休市'},
            {'active': 'true', 'day': 10, 'month': 4, 'year': 2021, 'bottomInfo': "创业板1季度预告结束", 'topInfo': '',
             'news': [{'desc': '深交所创业板2021年一季度预告披露结束', 'level': 10}]},
            {'active': 'true', 'day': 15, 'month': 4, 'year': 2021, 'bottomInfo': "深主板1季度预告结束", 'topInfo': '',
             'news': [{'desc': '深交所主板2021年一季度预告披露结束', 'level': 10}]},
            {'active': 'true', 'day': 29, 'month': 4, 'year': 2021, 'bottomInfo': "", 'topInfo': '美联储首次利率决议',
             'news': [{'desc': '2021年美联储首次利率决议', 'level': 10}]},
        ]}
        data = {
            'env': self.env,
            'query': """db.collection('calendar').add({})""".format(d)
        }
        print(data)
        rs = requests.post(url, data=json.dumps(data))
        print(rs.json())


if __name__ == '__main__':
    # rs = kp(l)
    # print(l, rs)
    db = CloudDb()
    db.add()

