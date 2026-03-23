from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

o = EdgeOptions()
o.add_experimental_option('detach',True)
driver = Edge(options=o)
driver.implicitly_wait(10)
driver.get('https://www.nike.in/')
driver.maximize_window()
kids = driver.find_element(By.XPATH,"//span[.='Kids']")
actions = ActionChains(driver)
actions.move_to_element(kids).pause(2).click(kids).perform()
# kids.click()
# sleep(3)
driver.switch_to.window(driver.window_handles[1])
elem = driver.find_element(By.XPATH,'//a[@aria-label="Shop"]')
actions.scroll_to_element(elem).pause(2).click(elem).perform()

img_click = driver.find_element(By.XPATH,'//div[@id="aria-label-24820896-1"]')
actions.scroll_to_element(img_click).pause(2).click(img_click).perform()
driver.switch_to.window(driver.window_handles[2])
click = driver.find_element(By.XPATH,"//label[text()='UK 13']")
actions.move_to_element(click).pause(2).click(click).perform()
add_to_cart = driver.find_element(By.XPATH,"//button[.='Add to Bag']")
actions.click(add_to_cart).perform()
driver.quit()