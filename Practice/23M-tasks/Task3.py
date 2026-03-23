from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

o = EdgeOptions()
o.add_experimental_option("detach",True)
driver = Edge(options=o)
driver.implicitly_wait(10)

driver.get('https://www.flipkart.com/')
driver.maximize_window()

driver.find_element(By.XPATH,"//span[@class='b3wTlE']").click()
myntra = driver.find_element(By.XPATH,"//a[.='Myntra']")
actions = ActionChains(driver)
actions.scroll_to_element(myntra).pause(2).click(myntra).perform()

driver.switch_to.window(driver.window_handles[1])
print(f'Page URL is {driver.current_url}')
print(f'Id is {driver.current_window_handle}')
print(f'Title is {driver.title}\n')

driver.switch_to.window(driver.window_handles[0])
cleartrip = driver.find_element(By.XPATH,"//a[.='Cleartrip']")
actions.scroll_to_element(cleartrip).pause(2).click(cleartrip).perform()

driver.switch_to.window(driver.window_handles[2])
print(f'Page URL is {driver.current_url}')
print(f'Id is {driver.current_window_handle}')
print(f'Title is {driver.title}\n')

driver.switch_to.window(driver.window_handles[0])
shopsy = driver.find_element(By.XPATH,"//a[.='Shopsy']")
actions.scroll_to_element(shopsy).pause(2).click(shopsy).perform()

driver.switch_to.window(driver.window_handles[3])
print(f'Page URL is {driver.current_url}')
print(f'Id is {driver.current_window_handle}')
print(f'Title is {driver.title}\n')

driver.quit()

