from selenium import webdriver
import time
path = "/Users/lifei/Downloads/chromedriver"
# path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
passwd = '1qaz@WSX'
users = [
# 'apollo',
# 'asm',
# 'bap',
'bap-auth',
# 'bpm',
# 'bps',
# 'cpm',
# 'cris',
# 'dec',
# 'east',
# 'ecm',
# 'egress',
# 'esb',
# 'eureka',
# 'fxq',
# 'gateway',
# 'hexincms',
# 'hexincmv7',
# 'hexinecif',
# 'hexinother',
# 'hexinutip',
# 'msg',
# 'nginx',
# 'odsc',
# 'pub',
# 'rpa',
# 'treasurer',
'uap-svc',
# 'xquant',
# 'xxljob',
# 'zabbix'
]


def brower():
    driver = webdriver.Chrome(path)
    # driver.get('https://www.baidu.com')
    driver.get('http://10.123.16.2:8888/mcloud/#/person/personList')
    print(driver.title)
    # time.sleep(100)
    # driver.find_element_by_name('q').send_keys('777777777')
    driver.find_element_by_id("account").send_keys('fcp')
    driver.find_element_by_id("password").send_keys('2w3e$R%T')
    a = input("wait...")
    print(a)
    # driver.find_element_by_id('kw').send_keys('test')
    # driver.find_element_by_id('su').click()
    iphone = '18612345'
    n = 1
    for u in users:
        y = input("check...")
        print(y)
        # driver.find_element_by_tag_name('新增').click()
        driver.find_element_by_id('userName').send_keys(u)
        driver.find_element_by_id('projectManager').click()
        driver.find_element_by_id('email').send_keys("{0}@chinaunicom.cn".format(u))
        driver.find_element_by_id('mobile').send_keys("{0}{1:03d}".format(iphone, n))
        driver.find_element_by_id('account').send_keys(u)
        driver.find_element_by_id('pwd').send_keys(passwd)
        # driver.find_element_by_link_text('提交').click()

        n += 1
    end = input("end...")
    driver.quit()


if __name__ == '__main__':
    brower()

