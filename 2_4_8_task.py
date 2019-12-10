from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser = webdriver.Chrome()
    # 1
    browser.get(link)
    # 2
    btn = browser.find_element_by_id("book")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    btn.click()
    # btn.click()
    # time.sleep(1)
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
    time.sleep(30)
    browser.quit()
    """
    answer:
    Congrats, you've passed the task! Copy this code as the answer to 
    Stepik quiz: 28.96437595544581
    """