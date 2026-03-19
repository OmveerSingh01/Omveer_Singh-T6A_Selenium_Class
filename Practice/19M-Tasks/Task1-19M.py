from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.by import By
o = EdgeOptions()
o.add_experimental_option('detach',True)
# o.add_argument('--headless')

driver = Edge(options=o)
driver.maximize_window()

driver.get('https://www.amazon.in/')
driver.implicitly_wait(15)
driver.find_element(By.ID,'twotabsearchtextbox').send_keys('Watch')
driver.find_element(By.ID,'nav-search-submit-button').click()

cnt_of_products = driver.find_elements(By.XPATH,"//div[@class='sg-col-4-of-4 sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 AdHolder sg-col s-widget-spacing-small sg-col-4-of-8 sg-col-4-of-20']")
print(len(cnt_of_products))


cnt_of_products[4].click()
# for i in range(0,5):
#     print(cnt_of_products[i].text)

driver.close()