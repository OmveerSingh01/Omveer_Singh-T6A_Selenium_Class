from time import sleep

from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common import keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

o = EdgeOptions()
o.add_experimental_option("detach",True)
driver = Edge(options=o)

driver.get('https://yonobusiness.sbi.bank.in/yonobusinesslogin')
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,"//span[@class='ng-tns-c2785778308-3 icon-cancel']").click()
sleep(2)
usern = driver.find_element(By.XPATH,"//input[@aria-label='User ID']").send_keys('Omveer')
password = driver.find_element(By.XPATH,"//input[@aria-label='PASSWORD']").send_keys('Om@12345')
eye = driver.find_element(By.XPATH,'//button[@tabindex="0"]')
actions = ActionChains(driver)
actions.pause(2).click_and_hold(eye).pause(5).release().perform()
