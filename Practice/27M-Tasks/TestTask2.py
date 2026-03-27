from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.ui import Select

o = EdgeOptions()
o.add_experimental_option('detach',True)
driver = Edge(options=o)
driver.implicitly_wait(20)
driver.get('https://demowebshop.tricentis.com/')
driver.maximize_window()

driver.find_element(By.XPATH,'//a[@href="/apparel-shoes"]').click()

def test_sort():
    sortBy = driver.find_element(By.XPATH,"//select[@id='products-orderby']")
    option = Select(sortBy)
    option.select_by_value('https://demowebshop.tricentis.com/apparel-shoes?orderby=11')

def test_disp():
    disp = driver.find_element(By.XPATH,"//select[@id='products-pagesize']")
    opt1 = Select(disp)
    opt1.select_by_index(2)

def test_view():
    view = driver.find_element(By.XPATH,"//select[@id='products-viewmode']")
    opt2 = Select(view)
    opt2.select_by_visible_text('List')

# driver.close()


