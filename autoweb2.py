from selenium import webdriver
import time
path = "/Users/lifei/Downloads/chromedriver"


def brower():
    driver = webdriver.Chrome(path)
    # driver.get('https://www.baidu.com')
    driver.get('http://127.0.0.1:8081/asset')
    print(driver.title)
    # driver.find_element_by_id('kw').send_keys("hw")
    # driver.find_element_by_css_selector("span[value=' 添 加 ']").click()
    driver.find_element_by_xpath("//span[text()='添 加']/..").click()
    driver.find_element_by_xpath("//div[@class='ant-col ant-form-item-control-wrapper']").click()
    driver.find_element_by_xpath("//div[@class='ant-form-item-control']").click()
    # 一个个试的哪个点击触发
    driver.find_element_by_xpath("//div[@class='ant-select ant-select-enabled']").click()
    # 鼠标移到下拉框，shift+command+c快捷键打开元素查看，点击下拉框，可以看到隐藏的元素
    driver.find_element_by_xpath("//*[text()=' 西红门 ']").click()
    # driver.find_element_by_xpath("//option[@value='西红门']").click()
    # s = driver.find_elements_by_tag_name("option")
    # print([i.tag_name for i in s])
    # s[1].click()
    # driver.find_element_by_xpath("//div[@class='ant-select-selection ant-select-selection--single']").click()
    time.sleep(100)
    driver.quit()


if __name__ == '__main__':
    brower()


