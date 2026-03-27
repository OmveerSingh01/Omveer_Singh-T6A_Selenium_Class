from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.by import  By

o = EdgeOptions()
o.add_experimental_option('detach',True)
driver = Edge(options=o)
driver.implicitly_wait(20)

driver.get('https://demowebshop.tricentis.com/')
driver.maximize_window()

def test_register():
    driver.find_element(By.XPATH,"//a[.='Register']").click()

def test_gender():
    driver.find_element(By.XPATH,"//input[@id='gender-male']").click()

def test_firstName():
    driver.find_element(By.XPATH,"//input[@id='FirstName']").send_keys('Omveer')

def test_lastName():
    driver.find_element(By.XPATH,"//input[@id='LastName']").send_keys('Singh')
def test_email():
    driver.find_element(By.XPATH,"//input[@id='Email']").send_keys('omveer@gmail.com')
def test_password():
    driver.find_element(By.XPATH,"//input[@id='Password']").send_keys('1234567')
def test_confirm():
    driver.find_element(By.XPATH,"//input[@id='ConfirmPassword']").send_keys('1234567')
def test_submit():
    driver.find_element(By.XPATH,"//input[@id='register-button']").click()

# driver.close()
