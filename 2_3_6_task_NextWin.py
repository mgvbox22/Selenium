import time
import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"
try:
    browser = webdriver.Chrome()
    # 1
    browser.get(link)
    # 2
    btn = browser.find_element_by_tag_name("button")
    btn.click()
    # btn.click()
    # time.sleep(1)
    # 3
    browser.switch_to.window(browser.window_handles[1])
    # 4
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    inp = browser.find_element_by_id("answer")
    inp.send_keys(y)
    btn = browser.find_element_by_css_selector('[type = "submit"]')
    btn.click()
    alert = browser.switch_to.alert
    print(alert.text)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
    """
    answer:
    Congrats, you've passed the task! Copy this code as the answer to 
    Stepik quiz: 28.9209760119497, 
    28.92098267735959
    """