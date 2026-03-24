from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.by import By
o= EdgeOptions()
o.add_experimental_option('detach',True)
driver = Edge(options=o)

driver.get('https://x.com/?lang=en-in')
driver.maximize_window()
sign = driver.find_element(By.XPATH,"//iframe[@title='Sign in with Google Button']")
driver.switch_to.frame(sign)
driver.find_element(By.XPATH,"//span[.='Sign up with Google']").click()
driver.close()