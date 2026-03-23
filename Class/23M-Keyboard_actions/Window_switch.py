from time import sleep

from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

o = EdgeOptions()
o.add_experimental_option("detach",True)
driver = Edge(options=o)
driver.get("https://www.google.com")
driver.maximize_window()
sleep(5)
# Manually open 3 tabs
print(driver.current_window_handle)  # This will give the address for current tab
print(driver.title)

print(driver.window_handles) # This will give the address for all the opened tabs

print(driver.switch_to.new_window())
driver.get("https://www.amazon.in/")
sleep(5)
print('After : ')
print(driver.title)
print(driver.current_window_handle)

driver.switch_to.window(driver.window_handles[0])
sleep(3)
driver.find_element(By.XPATH,'//a[@href="https://about.google/?fg=1&utm_source=google-IN&utm_medium=referral&utm_campaign=hp-header"]').click()
# driver.quit()