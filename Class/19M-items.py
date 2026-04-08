from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.by import By
o = EdgeOptions()
o.add_experimental_option('detach', True)
# o.add_argument('--headless')
driver = Edge(options=o)

driver.maximize_window()
# driver.get('https://www.google.com/')
driver.implicitly_wait(15)
# driver.find_element(By.TAG_NAME,'a').click()
# links = driver.find_elements(By.TAG_NAME,'a')
# print(links)
# for i in links:
#     print(i.text)

# ele = driver.find_element(By.XPATH,"//a[@class='gb_A']")
# print(ele.get_attribute('aria-label'))

# driver.get('https://www.amazon.in/')
# product = driver.find_elements(By.XPATH,"//div[@id='nav-main']//a")
# print(len(product))
# for item in range(0,len(product)):
#     print(f" {product[item].text} = {product[item].get_attribute('href')}")

# driver.get('https://www.facebook.com/')


# IS Functions
# ele = driver.find_element(By.XPATH,"//div[@aria-label='Log in']")
# print(ele.is_displayed())
# print(ele.is_enabled())
#
# btn = driver.find_element(By.XPATH,"//input[@type='submit']")
# print('Displayed :',btn.is_displayed())
# print('Enabled :',btn.is_enabled())

# driver.get('https://www.naukri.com/registration/createAccount?othersrcp=22636')
# sel = driver.find_element(By.XPATH,"//button[@type='submit']")
# print(f"Enabled :{sel.is_enabled()}")
# print(f"Displayed :{sel.is_displayed()}")

# driver.get('https://the-internet.herokuapp.com/checkboxes')
# chk = driver.find_element(By.XPATH,"//input[@type='checkbox'][1]")
# print(f"Selected : {chk.is_selected()}")
#
# driver.get('https://the-internet.herokuapp.com/checkboxes')
# chk = driver.find_element(By.XPATH,"//input[@type='checkbox'][2]")
# print(f"Selected : {chk.is_selected()}")



# driver.close()