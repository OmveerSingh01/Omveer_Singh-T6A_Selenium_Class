import pytest
from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

o = EdgeOptions()
o.add_experimental_option("detach", True)
driver = Edge(options=o)
wait = WebDriverWait(driver, 10)
driver.get('https://www.chennaisuperkings.com/')
driver.maximize_window()
driver.implicitly_wait(60)



@pytest.mark.smoke
def test_captain():
    driver.find_element(By.XPATH, '//a[.="TEAM"]').click()
    # cap = driver.find_element(By.XPATH,"(//div[.=' MS DHONI '])[1]").text
    cap = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'DHONI')]"))).text
    expected =  'MS DHONI'
    actual = cap
    assert expected == actual,"Captain Mismatch"
    print(f'Captain : {actual}')


@pytest.mark.smoke
def test_bowler():
    driver.find_element(By.XPATH, "(//a[.='SHOP'])[1]").click()
    # driver.find_element(By.XPATH, "(//div[.=' Fashion '])[1]").click()
    # wait.until(EC.presence_of_element_located(By.XPATH,'(//div[@class="text-containers"])[4]/child::div[.=" Fashion "]')).click()
    # wait.until(EC.presence_of_element_located((By.XPATH, '(//div[@class="text-containers"])[4]/child::div[.=" Fashion "]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Fashion')]"))).click()
    bow = driver.find_element(By.XPATH,'(//div[@class="col-12 col-lg-3 mb-3 d-flex"])[1]/descendant::p[.=" CSK Anbuden Polo "]').text
    expected = 'CSK Anbuden Polo'
    actual = bow
    assert expected == actual,"Product Name Mismatch"
    print(f'Product Name : {actual}')

@pytest.mark.regression
def test_price():
    driver.find_element(By.XPATH,"//a[.=' CSKTV ']").click()
    den = driver.find_element(By.XPATH,"//a[.=' Denside View ']").text
    expected = 'DENSIDE VIEW'
    actual = den
    assert expected == actual,"View Mismatch"
    print(f'View : {actual}')

@pytest.mark.regression
def test_name():
    driver.find_element(By.XPATH, "//a[.='TEAM']").click()
    driver.find_element(By.XPATH, '(//input[@label="Support Staff"])[2]').click()
    nme = driver.find_element(By.XPATH,"(//div[.=' MICHAEL HUSSEY '])[2]").text
    expected = 'MICHAEL HUSSEY'
    actual = nme
    assert expected == actual,"Name Mismatch"
    print(f'Name : {actual}')

# driver.close()
'''
For smoke testing run -> pytest .\Test_Task2.py -vs -m "smoke"
For regression testing run -> pytest .\Test_Task2.py -vs -m "regression"
'''
#
#


