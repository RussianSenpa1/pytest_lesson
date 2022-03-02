import pytest
from selenium.webdriver.common.by import By

class TestButton():
    def test_button(self, browser):
        browser.implicitly_wait(5) #Неявное ожидание, так как если инет слабый тест падает
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        button = browser.find_element(By.CLASS_NAME, 'btn8.btn-lg.btn-primary.btn-add-to-basket')
        assert button, 'Кнопка не найдена'

if __name__ == "__main__":
    pytest.main()