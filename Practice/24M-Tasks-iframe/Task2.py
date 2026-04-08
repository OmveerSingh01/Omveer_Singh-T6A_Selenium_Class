from time import sleep

from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.by import By
o= EdgeOptions()
o.add_experimental_option('detach',True)
driver = Edge(options=o)

driver.implicitly_wait(20)
driver.get('https://www.zomato.com/india')
driver.maximize_window()
driver.find_element(By.XPATH,"//a[.='Log in']").click()
# sleep(2)
email = driver.find_element(By.XPATH,"//iframe[@id='auth-login-ui']")
driver.switch_to.frame(email)
driver.find_element(By.XPATH,"//span[.='Sign in with Google']").click()
sleep(2)
driver.close()