from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.by import By
from time import sleep

o = EdgeOptions()
o.add_experimental_option('detach',True)
driver = Edge(options=o)
driver.implicitly_wait(50)
driver.get('https://www.amazon.in/')
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys("Toy cars")
sleep(5)
driver.find_element(By.XPATH,"//div[@id='sac-suggestion-row-4-cell-1']").click()

driver.find_element(By.XPATH,"//span[@id='a-autoid-0-announce']").click()
driver.find_element(By.XPATH,"//a[@id='s-result-sort-select_4']").click()
driver.find_element(By.XPATH,"//span[.='Free Shipping']").click()
sleep(3)

name = driver.find_element(By.XPATH, '(//div[@data-cy="title-recipe"])[1]').text
price = driver.find_element(By.XPATH, '(//span[@class="a-price-whole"])[1]').text


print(f'Name of Product :{name}')
print(f'Price of Product : Rs.{price}')
driver.close()