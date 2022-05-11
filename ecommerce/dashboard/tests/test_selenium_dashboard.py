import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

@pytest.mark.selenium
def test_create_new_admin(create_admin):
    assert create_admin.__str__() == 'admin'

@pytest.mark.selenium #Маркировка тестовых функций и отбор маркированных тестов для запуска
def test_dashboard_admin_login(live_server, create_admin, chrome_browser_instance): #live_server позволяет запустить сервер джанго в фоне
    browser = chrome_browser_instance


    browser.get(("%s%s" % (live_server.url, "/admin/login/")))

    user_name = browser.find_element(By.NAME, 'username')
    user_password = browser.find_element(By.NAME, 'password')
    submit = browser.find_element(By.XPATH, '//input[@value="Log in"]')

    user_name.send_keys('admin')
    user_password.send_keys('1')
    submit.send_keys(Keys.RETURN)

    assert 'Django administration' in browser.page_source