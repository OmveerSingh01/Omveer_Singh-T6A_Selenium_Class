import pytest
from selenium import webdriver
from sheet02 import get_test_data
from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.by import By

# o = EdgeOptions()
# o.add_experimental_option("detach", True)
# driver = Edge(options=o)

@pytest.fixture(autouse=True)
def openBrowser():
    o = EdgeOptions()
    o.add_experimental_option("detach", True)
    # global driver
    driver = Edge(options=o)
    driver.get('https://www.saucedemo.com/')
    driver.maximize_window()
    driver.implicitly_wait(60)
    print('Opening Browser')
    yield driver
    print('Closing Browser')
    driver.close()


@pytest.mark.parametrize('user,passwd',get_test_data())
def test_login(openBrowser, user,passwd):
    openBrowser.find_element(By.XPATH,'//input[@id="user-name"]').send_keys(user)
    openBrowser.find_element(By.XPATH,'//input[@id="password"]').send_keys(passwd)
    openBrowser.find_element(By.XPATH,'//input[@id="login-button"]').click()
    expected = 'https://www.saucedemo.com/inventory.html'
    actual = openBrowser.current_url
    assert expected == actual,"Login Failed"