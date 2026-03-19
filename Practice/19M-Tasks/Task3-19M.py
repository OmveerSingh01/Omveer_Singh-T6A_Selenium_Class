from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.by import By
o = EdgeOptions()
o.add_experimental_option('detach', True)
# o.add_argument('--headless')
driver = Edge(options=o)

driver.maximize_window()
driver.implicitly_wait(15)

driver.get("https://demowebshop.tricentis.com/")
driver.find_element(By.XPATH,"//a[text()='Register']").click()
driver.find_element(By.XPATH,"//input[@id='gender-male']").click()
driver.find_element(By.XPATH,"//input[@id='FirstName']").send_keys("Omveer")
driver.find_element(By.XPATH,"//input[@id='LastName']").send_keys("Singh")
driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("Om121@gmail.com")
driver.find_element(By.XPATH,"//input[@id='Password']").send_keys("Omveer123")
driver.find_element(By.XPATH,"//input[@id='ConfirmPassword']").send_keys("Omveer123")
driver.find_element(By.XPATH,"//input[@id='register-button']").click()
driver.close()



