from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

o= EdgeOptions()
o.add_experimental_option('detach',True)
driver = Edge(options=o)

driver.get('file:///D:/Selenium_Training_py/Class_Work/Selenium_capgemini/Class/24M-Frames/page1.html')
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='in1']").send_keys("Input 1")

# driver.switch_to.frame(0) # Using Indexing -------- We are switching into page 2 by using indexing
# driver.switch_to.frame('n11') # Using name ----------------We are switching into page 2 by using name
driver.switch_to.frame('frame1')  # Using ID

driver.find_element(By.XPATH,"//input[@id='in2']").send_keys("Input 2")
# driver.switch_to.frame('n12')  # We are switching into page 2 by using name

driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='frame2']")) # Using Xpath
driver.find_element(By.XPATH,"//input[@id='in3']").send_keys("Input 3")

driver.switch_to.parent_frame()
sleep(2)
driver.find_element(By.XPATH,"//input[@id='in2']").clear()
sleep(2)
driver.find_element(By.XPATH,"//input[@id='in2']").send_keys(" Back to Page 2")

driver.switch_to.parent_frame()
sleep(2)
driver.find_element(By.XPATH,"//input[@id='in1']").clear()
sleep(2)
driver.find_element(By.XPATH,"//input[@id='in1']").send_keys(" Back to Page 1")

driver.switch_to.default_content()
sleep(2)
driver.find_element(By.XPATH,"//input[@id='in1']").clear()
