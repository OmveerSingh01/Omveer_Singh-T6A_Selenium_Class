from time import sleep

from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

o = EdgeOptions()
o.add_experimental_option("detach",True)
driver = Edge(options=o)

'''driver.get('https://www.amazon.com/')
driver.maximize_window()
sleep(2)
ele = driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']")
ele.send_keys('shoes')
ele.send_keys(Keys.ENTER)'''

driver.get('https://demoqa.com/text-box')
ele = driver.find_element(By.XPATH,"//textarea[@id='currentAddress']")
ele.send_keys('Parbatsar,Rajasthan')
ele.send_keys(Keys.CONTROL+'a')
ele.send_keys(Keys.CONTROL+'c')

ele = driver.find_element(By.XPATH,"//textarea[@id='permanentAddress']")
ele.send_keys(Keys.CONTROL+'v')