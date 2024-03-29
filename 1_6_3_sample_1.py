from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit")
    button.click()
except Exception as ex:
    print("Exception:", ex)
    input()
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()