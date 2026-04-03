import pytest
from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.by import By

o = EdgeOptions()
o.add_experimental_option("detach", True)
driver = Edge(options=o)

@pytest.mark.parametrize('user,passwd',[('standard_user','secret_sauce'),('locked_out_user','secret_sauce'),('error_user','secret_sauce')])
def test_login(user,passwd):
    driver.get('https://www.saucedemo.com/')
    driver.maximize_window()
    driver.implicitly_wait(60)
    driver.find_element(By.XPATH,'//input[@id="user-name"]').send_keys(user)
    driver.find_element(By.XPATH,'//input[@id="password"]').send_keys(passwd)
    driver.find_element(By.XPATH,'//input[@id="login-button"]').click()

