from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o= ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
# driver.get("https://demoqa.com/text-box")
#
# driver.maximize_window()
# sleep(2)
#
# driver.find_element(By.XPATH,"//input[@placeholder='Full Name']").send_keys("akshay")
# # driver.find_element(By.XPATH,"//input[text()='Email']").send_keys("abc@gmail")
# sleep(2)
# driver.find_element(By.XPATH,"//button[.='Submit']").click()

driver.get("https://www.amazon.in")
driver.maximize_window()
sleep(2)

# driver.find_element(By.XPATH,"//span[contains(.,'vases')]").click()  #using contains text
# driver.find_element(By.XPATH,"//span[contains(text(),'vases')]").click()  #using contains text()


sleep(15)
driver.quit()