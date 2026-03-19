from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.by import By
o = EdgeOptions()
o.add_experimental_option('detach', True)
# o.add_argument('--headless')
driver = Edge(options=o)

driver.maximize_window()
driver.implicitly_wait(15)

driver.get('https://testautomationpractice.blogspot.com/')
driver.find_element(By.XPATH,"//input[@id='singleFileInput']").send_keys(r"C:\Users\Omveer\Downloads\Admit Card.pdf")
driver.find_element(By.XPATH,"//input[@id='multipleFilesInput']").send_keys(r"C:\Users\Omveer\OneDrive\사진\Screenshots\Screenshot 2024-11-20 125331.png")
driver.find_element(By.XPATH,"//input[@id='multipleFilesInput']").send_keys(r"C:\Users\Omveer\OneDrive\사진\Screenshots\Screenshot 2024-11-21 020808.png")
# driver.close()
