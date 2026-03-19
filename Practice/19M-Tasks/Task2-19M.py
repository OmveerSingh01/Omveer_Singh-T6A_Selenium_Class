from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.by import By
o = EdgeOptions()
o.add_experimental_option('detach', True)
# o.add_argument('--headless')
driver = Edge(options=o)

driver.maximize_window()
driver.implicitly_wait(15)

driver.get('https://demoqa.com/automation-practice-form')
driver.find_element(By.XPATH,"//input[@id='firstName']").send_keys('Omveer')
driver.find_element(By.XPATH,"//input[@id='lastName']").send_keys('Singh')
driver.find_element(By.XPATH,"//input[@class='mr-sm-2 form-control']").send_keys('Om@gmail.com')
driver.find_element(By.XPATH,"//input[@id='gender-radio-1']").click()
driver.find_element(By.XPATH,"//input[@id='userNumber']").send_keys('9898111100')
driver.find_element(By.XPATH,"//input[@id='dateOfBirthInput']").click()
driver.find_element(By.XPATH,"//div[@class='react-datepicker__year-dropdown-container react-datepicker__year-dropdown-container--select']").click()
driver.find_element(By.XPATH,"//option[text()=2000]").click()
driver.find_element(By.XPATH,"//select[@class='react-datepicker__month-select']").click()
driver.find_element(By.XPATH,"//option[@value='9']").click()
driver.find_element(By.XPATH,"//div[text()='11']").click()

# driver.find_element(By.XPATH,"//div[@class='subjects-auto-complete__input-container css-19bb58m']").send_keys('maths,english')
driver.find_element(By.XPATH,"//input[@id='hobbies-checkbox-3']").click()
driver.find_element(By.XPATH,"//input[@id='hobbies-checkbox-1']").click()
driver.find_element(By.XPATH,"//input[@id='uploadPicture']").send_keys(r"C:\Users\Omveer\Downloads\Admit Card.pdf")

driver.find_element(By.XPATH,"//textarea[@id='currentAddress']").send_keys('Jaipur')
driver.find_element(By.XPATH,"//div[@class='css-19bb58m']").click()
driver.close()