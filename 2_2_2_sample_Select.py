import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select # for method 3

link = "file:///D:/_Doc/QA/HTML/radiobutton.html"
""" # SAMPLE
    <label for="dropdown">Выберите язык программирования:</label>
    <select id="dropdown" class="custom-select">
        <option selected>--</option>
        <option value="1">Python</option>
        <option value="2">Java</option>
        <option value="3">JavaScript</option>
    </select>
"""
try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_tag_name("select").click()
    # selecting "Python" in sample
    # method I
    # browser.find_element_by_css_selector("option:nth-child(2)").click()
    # method II
    # browser.find_element_by_css_selector("[value='1']").click()
    # method III
    select = Select(browser.find_element_by_tag_name("select"))
    # III.I
    # select.select_by_value("1")  # ищем элемент с текстом "Python"
    # III.II
    # select.select_by_visible_text("Python")
    # III.III
    select.select_by_index(1)  # counting starts from 0

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()