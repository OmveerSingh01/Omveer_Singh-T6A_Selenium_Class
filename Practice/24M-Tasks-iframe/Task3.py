from time import sleep

from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.by import By
o = EdgeOptions()
o.add_experimental_option('detach',True)
driver = Edge(options=o)
driver.maximize_window()

# driver.switch_to.new_window()
driver.get("https://myntra.com")
print(f'First tab title : {driver.title}')
print(f'URL : {driver.current_url}\n')

driver.switch_to.new_window()
driver.get("https://district.in")
print(f'Second tab title : {driver.title}')
print(f'URL : {driver.current_url}\n')

driver.switch_to.new_window()
driver.get("https://groww.in")
print(f'Third tab title : {driver.title}')
print(f'URL : {driver.current_url}\n')
sleep(2)
driver.close()

sleep(2)
driver.switch_to.window(driver.window_handles[1])
driver.close()

sleep(2)
driver.switch_to.window(driver.window_handles[0])
