import os
import time

from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.by import By
from time import sleep
o= EdgeOptions()
o.add_experimental_option('detach',True)
driver = Edge(options=o)

# driver.get("https://google.com")
driver.maximize_window()
# print(driver.title)
# sleep(2)

'''expected = 'Google'
actual = driver.title
assert expected == actual,"Title mismatch"
# If expected condition does not match with actual result then test falils and it will not continue further and give assertion error.

driver.find_element(By.XPATH,"//textarea[@title='Search']").send_keys("CSK Dhoni")'''
# sleep(2)

driver.get("https://amazon.in/")
driver.implicitly_wait(100)
driver.find_element(By.XPATH,"//a[.='Bestsellers']").click()
expected = 'Amazon.in Bestsellers: The most popular items on Amazon'
actual = driver.title
assert expected == actual,"Title mismatch"
# driver.save_screenshot('screenshot1.png')

folder = os.path.join(os.getcwd(), 'screenshot')
os.makedirs(folder,exist_ok=True)
driver.save_screenshot(f'{folder}/screenshot_page.png')

ele = driver.find_element(By.XPATH,'//input[@id="twotabsearchtextbox"]')
'''ele.screenshot(f'{folder}/screenshot_element.png')
ele.send_keys('Omveer')
ele.screenshot(f'{folder}/screenshot_om.png')'''

timestamp = time.strftime("%Y%m%d-%H%M%S")
ele.screenshot(f'{folder}/screenshot_{timestamp}.png')
sleep(5)
# driver.quit()
