import time
import os
from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
o = EdgeOptions()
o.add_experimental_option('detach',True)
driver = Edge(options=o)

driver.get('https://www.pinterest.com/')
driver.maximize_window()
driver.implicitly_wait(20)

folder = os.path.join(os.getcwd(),"Pinterest_ss")
os.makedirs(folder,exist_ok=True)

driver.save_screenshot(f'{folder}/Pinterest_1.png')

ele = driver.find_element(By.XPATH,'//img[@src="https://s.pinimg.com/webapp/visual-search-1px-ecc706bc.png"]')
action = ActionChains(driver)
action.move_to_element(ele).pause(2).perform()


timestamp = time.strftime("%Y%m%d-%H%M%S")
ele.screenshot(f'{folder}/Pinterest2_{timestamp}.png')
sleep(2)
driver.quit()


