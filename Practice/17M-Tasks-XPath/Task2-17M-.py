from selenium.webdriver import Chrome, ChromeOptions
# from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.implicitly_wait(10)
driver.get('https://demoqa.com/webtables')
wait = WebDriverWait(driver,100)
# wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='addNewRecordButton']"))).click()
# wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='firstName']"))).send_keys('Omveer')
# wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='lastName']"))).send_keys('Singh')
# wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='userEmail']"))).send_keys('Om@123gmail.com')
# wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='age']"))).send_keys('22')
# wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='salary']"))).send_keys('78000')
# wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='department']"))).send_keys('IT')
# wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='submit']"))).click()
name =  wait.until(EC.visibility_of_element_located((By.XPATH,"//td[text()='Omveer']")))
salary = wait.until(EC.visibility_of_element_located((By.XPATH,"//td[text()='Omveer']/../td[5]")))


print(f'Salary of {name.text} is {salary.text}')
# sleep(2)
driver.quit()