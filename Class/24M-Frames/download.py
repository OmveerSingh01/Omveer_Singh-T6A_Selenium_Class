from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


o= ChromeOptions()
o.add_experimental_option('detach',True)
o.add_experimental_option('prefs',{"safebrowsing.enabled":True})
o.add_argument('--disable-notifications')
driver = Chrome(options=o)
driver.implicitly_wait(20)

# driver.get('https://www.python.org/downloads/')
# driver.maximize_window()
# driver.find_element(By.XPATH,"(//a[.='Python 3.14.3'])[4]").click()

# driver.get('https://www.easemytrip.com/')
# driver.maximize_window()

# driver.get('https://www.irctc.co.in/nget/train-search')
# driver.maximize_window()
# driver.find_element(By.XPATH,"(//input[@type='text'])[3]").click()
# driver.find_element(By.XPATH,'//a[@class="ui-datepicker-next ui-corner-all ng-tns-c69-9 ng-star-inserted"]').click()
# driver.find_element(By.XPATH,"//span[.='April']").click()
# driver.find_element(By.XPATH,"//a[.='15']").click()

driver.get('https://demoqa.com/automation-practice-form')
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='dateOfBirthInput']").click()
driver.find_element(By.XPATH,"//select[@class='react-datepicker__month-select']").click()
driver.find_element(By.XPATH,"//option[.='November']").click()
driver.find_element(By.XPATH,'//select[@class="react-datepicker__year-select"]').click()
driver.find_element(By.XPATH,"//option[.='2027']").click()
driver.find_element(By.XPATH,"(//div[.='11'])[1]").click()


