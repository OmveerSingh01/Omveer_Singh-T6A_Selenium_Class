from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

o= EdgeOptions()
o.add_experimental_option('detach',True)
driver = Edge(options=o)

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
alr = driver.find_element(By.XPATH,"//button[.='Simple Alert']")
actions = ActionChains(driver)
actions.scroll_to_element(alr).pause(2).click(alr).pause(2).perform()

alert = driver.switch_to.alert
# alert.accept()  #This is used to accept the alert box
alert.dismiss() # Used to cancel the alert box

conf = driver.find_element(By.XPATH,"//button[.='Confirmation Alert']")
actions.scroll_to_element(conf).pause(2).click(conf).perform()
driver.switch_to.alert.accept()

prom = driver.find_element(By.XPATH,"//button[.='Prompt Alert']")
actions.scroll_to_element(prom).pause(2).click(prom).perform()
driver.switch_to.alert.send_keys('Omveer')
driver.switch_to.alert.accept()