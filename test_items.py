import pytest
from selenium.webdriver.common.by import By

class Test():
    def test_link(self, browser):
        browser.implicitly_wait(5)
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        browser.find_element(By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')

if __name__ == "__main__":
    pytest.main()