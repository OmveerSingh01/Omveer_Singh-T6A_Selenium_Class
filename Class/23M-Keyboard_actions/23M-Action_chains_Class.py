'''
Action Chain Class
1. Create Object
2. Store Action
3. Perform
'''

from time import sleep

from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common import keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

o = EdgeOptions()
o.add_experimental_option("detach",True)
driver = Edge(options=o)

'''driver.get('https://demoqa.com/buttons')
driver.maximize_window()
# driver.find_element
sing_click = driver.find_element(By.XPATH,"//button[text()='Click Me']")
right_click = driver.find_element(By.XPATH,"//button[.='Right Click Me']")
doub_click = driver.find_element(By.XPATH,"//button[.='Double Click Me']")

actions = ActionChains(driver)
actions.click(sing_click).perform()
sleep(2)
actions.double_click(doub_click).perform()
sleep(2)
actions.context_click(right_click).perform()
sleep(2)
actions.click(sing_click).perform()'''


# driver.find_element(By.ID,'doubleClickBtn').click()
# driver.find_element(By.ID,'rightClickBtn').click()
# driver.find_element(By.XPATH,"//button[text()='Click Me']").click()

# ------------------------------------------------------------------
# driver.implicitly_wait(100)
# driver.get('https://www.amazon.in/')
# driver.maximize_window()
# # sleep(3)
# actions = ActionChains(driver)
# ele = driver.find_element(By.XPATH,'(//span[@class="a-list-item"])[5]')
# actions.pause(2).scroll_to_element(ele).pause(2).perform().pause(2).click().perform()

# ------------------------------------------------------------------
# actions.pause(5).scroll_by_amount(0,1000).perform()
# sleep(2)
# If we give scroll by amount again after a scroll by amount then it will scroll from the previous one's endpoint
# actions.pause(5).scroll_by_amount(0,400).perform()
# actions.pause(5).scroll_by_amount(0,400).perform()
# sleep(2)

# -------------------------------------------------------------------
'''kid = driver.find_element(By.XPATH,"//span[@class='a-list-item']")
origin  = ScrollOrigin.from_element(kid)
sleep(2)
actions.pause(2).scroll_from_origin(origin,0,1000).perform()'''

# -----------------------------------------------------------------
# Drag and Drop
driver.get('https://demoqa.com/droppable')
drg = driver.find_element(By.XPATH,"//div[@id='draggable']")
drp = driver.find_element(By.XPATH,"//div[@id='droppable']")
actions = ActionChains(driver)
actions.pause(2).drag_and_drop(drg,drp).perform()
# driver.close()