from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common import keys

o = EdgeOptions()
o.add_experimental_option("detach",True)
driver = Edge(options=o)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
actions = ActionChains(driver)

ele = driver.find_element(By.XPATH,"//button[text()='Point Me']")
actions.move_to_element(ele).pause(2).click().perform()

dub_click = driver.find_element(By.XPATH,"//button[text()='Copy Text']")
actions.double_click(dub_click).perform()
sleep(2)

drg = driver.find_element(By.XPATH,"//div[@id='draggable']")
drp = driver.find_element(By.XPATH,"//div[@id='droppable']")
actions.pause(2).drag_and_drop(drg,drp).perform()

driver.close()