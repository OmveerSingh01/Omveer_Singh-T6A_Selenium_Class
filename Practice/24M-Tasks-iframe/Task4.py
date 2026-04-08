from time import sleep

from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
o = EdgeOptions()
o.add_experimental_option("detach", True)
driver = Edge(options=o)

driver.maximize_window()
driver.get('https://the-internet.herokuapp.com/javascript_alerts')

alr = driver.find_element(By.XPATH,"//button[.='Click for JS Alert']")
actions = ActionChains(driver)
actions.scroll_to_element(alr).click(alr).perform()
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()
sleep(2)

conf = driver.find_element(By.XPATH,"//button[.='Click for JS Confirm']")
actions.scroll_to_element(conf).click(conf).perform()
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()
# driver.switch_to.alert.accept()
sleep(2)

prom = driver.find_element(By.XPATH,"//button[.='Click for JS Prompt']")
actions.scroll_to_element(prom).click(prom).perform()
print(driver.switch_to.alert.text)
driver.switch_to.alert.send_keys('Omveer')
driver.switch_to.alert.accept()
sleep(2)

driver.close()
