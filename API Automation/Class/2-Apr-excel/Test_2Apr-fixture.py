import pytest
from selenium import webdriver
from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.by import By

# o = EdgeOptions()
# o.add_experimental_option("detach", True)
# driver = Edge(options=o)




@pytest.mark.parametrize('user,passwd',[('standard_user','secret_sauce'),('locked_out_user','secret_sauce'),('visual_user','secret_sauce')])
def test_login(openBrowser, user,passwd):
    openBrowser.find_element(By.XPATH,'//input[@id="user-name"]').send_keys(user)
    openBrowser.find_element(By.XPATH,'//input[@id="password"]').send_keys(passwd)
    openBrowser.find_element(By.XPATH,'//input[@id="login-button"]').click()
    expected = 'https://www.saucedemo.com/inventory.html'
    actual = openBrowser.current_url
    assert expected == actual,"Login Failed"