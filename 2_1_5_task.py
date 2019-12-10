import math
import time
from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    # 1
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # 2
    x_elem = browser.find_element_by_id("input_value")
    x = x_elem.text
    # 3
    y = calc(x)
    # 4
    inp = browser.find_element_by_id("answer")
    inp.send_keys(y)
    # 5
    cb = browser.find_element_by_id("robotCheckbox")
    cb.click()
    # 6
    rb = browser.find_element_by_id("robotsRule")
    rb.click()
    # 7
    btn = browser.find_element_by_css_selector('[type = "submit"]')
    btn.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
    """
    Congrats, you've passed the task!
    Copy this code as the answer to 
    Stepik quiz: 28.829299736487457
    """