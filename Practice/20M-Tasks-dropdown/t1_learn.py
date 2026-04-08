from time import sleep

import driver
from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

o = EdgeOptions()
o.add_experimental_option('detach',True)
# driver.implicitly_wait(5)
driver = Edge(options=o)
driver.get('https://www.zomato.com/jaipur/restaurants"')
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='keywords_input']").send_keys('Dosa')
driver.find_element(By.XPATH,"//div[@id='search_button']").click()
dropdown = driver.find_elements(By.XPATH,"//div[@id='keywords-dd']")
# option = Select(dropdown)
# option.select_by_visible_text("Green Dosa")
# option.select_by_value("")

sleep(3)

for  i in range(len(dropdown)):
    print(dropdown[i].text)