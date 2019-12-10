
import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"
try:
    browser = webdriver.Chrome()
    # 1
    browser.get(link)
    # 2
    btn = browser.find_element_by_css_selector("button.btn-primary")
    btn.click()
    # 3
    alert = browser.switch_to.alert
    alert.accept()
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
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    # time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
    """
    answer:
    Congrats, you've passed the task! Copy this code as the answer to 
    Stepik quiz: 28.92010585720149
    """