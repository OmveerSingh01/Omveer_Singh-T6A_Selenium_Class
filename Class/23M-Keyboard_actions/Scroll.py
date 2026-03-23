from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.maximize_window()

'''driver.get("https://demoqa.com/buttons")

driver.implicitly_wait(10)
actions = ActionChains(driver)

doubleClick = driver.find_element(By.XPATH, '//button[@id="doubleClickBtn"]')
actions.double_click(doubleClick).perform()

rightClick = driver.find_element(By.XPATH, '//button[@id="rightClickBtn"]')
actions.context_click(rightClick).perform()

singleClick = driver.find_element(By.XPATH, '//button[.="Click Me"]')
actions.click(singleClick).perform()'''


# Scroll to the element function in action chain
driver.get("https://amazon.in/")

driver.implicitly_wait(100)
actions = ActionChains(driver)

bikeImg = driver.find_element(By.XPATH, '//img[@src="https://m.media-amazon.com/images/I/71eCO4ULXfL._AC_SY200_.jpg"]')
actions.scroll_to_element(bikeImg).pause(2).click(bikeImg).perform()