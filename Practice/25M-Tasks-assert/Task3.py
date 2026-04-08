from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.by import By
from time import sleep
import os

o = EdgeOptions()
o.add_experimental_option('detach',True)
driver = Edge(options=o)
o.add_argument('--disable-notifications')
driver.implicitly_wait(60)
driver.get('https://www.lenskart.com/')
driver.maximize_window()

eye = driver.find_element(By.XPATH,"//a[@id='lrd1']").click()
expected = 'https://www.lenskart.com/eyeglasses.html'
actual = driver.current_url
assert expected == actual,"URl Mismatch"

driver.find_element(By.XPATH,"//select[@id='sortByDropdown']").click()
driver.find_element(By.XPATH,"//option[.='Most Viewed']").click()
# sleep(5)
folder = os.path.join(os.getcwd(),'Lenskart_ss')
os.makedirs(folder,exist_ok=True)
driver.save_screenshot(f'{folder}/ss_lenskart.png')

driver.close()


