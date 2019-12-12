import unittest
import time
from selenium import webdriver


class MyTestCase(unittest.TestCase):
    def test_link1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.__registration(link)

    def test_link2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.__registration(link)

    def __registration(self, link):
        browser = webdriver.Chrome()
        browser.get(link)
        # my code
        selectors = [".first_block input.first", ".first_block input.second", ".first_block input.third"]
        value = ["First", "Second", "Third"]
        for i in range(len(selectors)):
            element = browser.find_element_by_css_selector(selectors[i])
            element.send_keys(value[i])
        time.sleep(3)
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(3)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        # assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == '__main__':
    unittest.main()
    input()
    """ answer:
    FAILED (errors=1)
    """