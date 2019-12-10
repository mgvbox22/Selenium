import math
import time
from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    # 1
    link = "http://suninjuly.github.io/execute_script.html"
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
    btn = browser.find_element_by_css_selector('[type = "submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
    # 7
    rb = browser.find_element_by_id("robotsRule")
    rb.click()
    # 8

    btn.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
    """
    Congrats, you've passed the task! Copy this code as the answer to 
    Stepik quiz: 28.87654233399416
    """