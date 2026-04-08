from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.by import By
from time import sleep

o = EdgeOptions()
o.add_experimental_option('detach',True)
driver= Edge(options=o)

# driver.get('https://www.amazon.in/')
# sleep(4)
# driver.find_element(By.ID,'twotabsearchtextbox').send_keys('mobiles')
# # sleep(2)
# driver.find_element(By.ID,'nav-search-submit-button').click()
#
# sleep(3)
# driver.find_element(By.XPATH,'//h2[contains(@aria-label,"iPhone 17")]')
# print(driver.find_element(By.XPATH,'//span[@class="a-price-whole"]').text)
# //span[contains(text(),'iQOO Z10x 5G (Ultramarine, 8GB RAM, 256GB Storage)')]/../../../..//span[@class='a-price-whole']

# print(driver.find_element(By.XPATH,"(//span[contains(text(),'Samsung Galaxy M07 Mobile (Black, 4GB RAM, 64GB Storage) |')]/../../../..//span)[9]").text)

driver.get('https://www.flipkart.in/')
sleep(5)
driver.find_element(By.CLASS_NAME,"nw1UBF.v1zwn25").send_keys("Pen")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
sleep(3)
# print(driver.find_element(By.XPATH,"(//a[contains(text(),'Reynolds DFine Ball Pen')]/../a)[3]").text)
d= driver.find_element(By.XPATH,"//a[contains(@title, 'Reynolds')]/..//div[@class='hZ3P6w']")
print(d.text)


# driver.find_element(By.CLASS_NAME,"").click()
driver.quit()
