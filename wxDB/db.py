import requests
import json
import os


class CloudDb(object):
    def __init__(self, config):
        conf = open(config)
        appid, secret, env = [i.replace('\n', '') for i in conf.readlines()]
        self.url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'.format(appid, secret)
        self.tk = self.token()
        self.env = env

    def token(self):
        rs = requests.get(self.url).json()
        return rs

    def add(self):
        url = 'https://api.weixin.qq.com/tcb/databaseadd?access_token={}'.format(self.tk.get('access_token', ''))
        d = {'data': [
            {'active': 'true', 'day': 5, 'month': 5, 'year': 2022, 'bottomInfo': "美4月就业数据", 'topInfo': '美联储利率决议',
             'news': [{'desc': '美国4月ADP就业数据', 'level': 1}, {'desc': '美联储利率决议', 'level': 10}]},
        ]}
        data = {
            'env': self.env,
            'query': """db.collection('calendar').add({})""".format(d)
        }
        rs = requests.post(url, data=json.dumps(data))
        print(rs.json())

    def add_market(self, sh, sz):
        """ 添加每天行情信息 """
        url = 'https://api.weixin.qq.com/tcb/databaseadd?access_token={}'.format(self.tk.get('access_token', ''))
        d = {'data': [
            {'sz': sz, 'sh': sh, 'date': sh.get("date")}
        ]}
        data = {
            'env': self.env,
            'query': """db.collection('market').add({})""".format(d)
        }
        rs = requests.post(url, data=json.dumps(data))
        print(rs.json())

    def update_market(self, sh, sz):
        """ 更新每日行情, 如果指定的记录不存在，则会自动创建该记录"""
        url = 'https://api.weixin.qq.com/tcb/databaseupdate?access_token={}'.format(self.tk.get('access_token', ''))
        date = sh.get('date', '')
        d = {'data': {'sz': sz, 'sh': sh, 'date': date}}
        data = {
            'env': self.env,
            'query': """db.collection('market').doc('{}').set({})""".format(date, d)
        }
        rs = requests.post(url, data=json.dumps(data))
        rs = rs.json()
        # token过期重新获取
        # {'errcode': 42001, 'errmsg': 'access_token expired rid: 627ca5cf-7e811ede-0fbc1f73'}
        if "access_token expired" in rs.get("errmsg", ''):
            self.tk = self.token()
            url = 'https://api.weixin.qq.com/tcb/databaseupdate?access_token={}'.format(self.tk.get('access_token', ''))
            rs = requests.post(url, data=json.dumps(data)).json()
        print(rs)

    def search_market(self, date):
        """ 按日期查找行情 """
        url = 'https://api.weixin.qq.com/tcb/databasequery?access_token={}'.format(self.tk.get('access_token', ''))
        data = {
            'env': self.env,
            'query': """db.collection('market').where({{date: '{}'}}).get()""".format(date)
        }
        rs = requests.post(url, data=json.dumps(data))
        return rs.json()


if __name__ == '__main__':
    db = CloudDb(config='{}/config.pk'.format(os.getcwd()))
    # db.add()
    r = db.search_market("2022-5-29")
    print(r)
