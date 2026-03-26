import os
import time

from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.by import By
from time import sleep
o= EdgeOptions()
o.add_experimental_option('detach',True)
driver = Edge(options=o)

driver.get('https://www.saucedemo.com')
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys('standard_user')
driver.find_element(By.XPATH,"//input[@id='password']").send_keys('12345')
driver.find_element(By.XPATH,"//input[@type='submit']").click()

expected = 'https://www.saucedemo.com/inventory.html'
actual = driver.current_url

folder = os.path.join(os.getcwd(), 'screenshot')
os.makedirs(folder,exist_ok=True)
try:
    assert expected == actual,"URL Mismatch"
except AssertionError:
    driver.save_screenshot(f'{folder}/screenshot_urlPage.png')


