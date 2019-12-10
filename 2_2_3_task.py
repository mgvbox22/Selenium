import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select # for method 3

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    elem1 = browser.find_element_by_id("num1")
    elem2 = browser.find_element_by_id("num2")
    print(elem1.text, elem2.text)
    result = str(int(elem1.text)+int(elem2.text))
    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_visible_text(result)
    btn = browser.find_element_by_css_selector('[type = "submit"]')
    btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
    """
    answer: Congrats, you've passed the task! Copy this code as the answer for 
    Stepik quiz: 28.87500113719794
    """