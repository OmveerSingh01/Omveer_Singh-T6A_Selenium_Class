from time import sleep

from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Edge()

o = EdgeOptions()
o.add_experimental_option('detach',True)
driver= Edge(options=o)

driver.implicitly_wait(5)
wait = WebDriverWait(driver,10)

driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/dynamic_loading")
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//a[text()='Example 1: Element on page that is hidden']").click()
driver.find_element(By.XPATH,"//button[text()='Start']").click()

ele = wait.until(EC.visibility_of_element_located((By.XPATH,"//h4[contains(text(),'Hello')]")))
print(ele.text)

# sleep(5)
# prt = driver.find_element(By.XPATH,"//h4[text()='Hello World!']").text
# print(prt)
driver.quit()

# driver.get("https://www.decathlon.in/")
# driver.implicitly_wait(10)
# # sleep(3)
# driver.find_element(By.XPATH,"//a[@href='https://www.decathlon.in/shop/Winter-Collection']").click()
# # sleep(3)
# driver.find_element(By.XPATH,"//a[@href='https://www.decathlon.in/c/jackets-26192']").click()


