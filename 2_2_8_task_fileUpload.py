import os
import time
from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"


fname = "2_2_8_fileUpload.txt"
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, fname)           # добавляем к этому пути имя файла

try:
    browser = webdriver.Chrome()
    browser.get(link)
    selectors = ['input[name="firstname"]',
                 'input[name="lastname"]',
                 'input[name="email"]' ]
    value = ["FN", "SN", "e@m"]
    for i in range(len(selectors)):
        element = browser.find_element_by_css_selector(selectors[i])
        element.send_keys(value[i])
    sel_file = browser.find_element_by_css_selector("input#file")
    # sel_file.click()
    sel_file.send_keys(file_path)

    btn = browser.find_element_by_css_selector('[type = "submit"]')
    btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
    """
    answer: 
    Congrats, you've passed the task! Copy this code as the answer for
     Stepik quiz: 28.87745467437076
    """