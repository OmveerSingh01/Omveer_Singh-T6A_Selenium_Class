import pytest
from selenium.webdriver import Edge,EdgeOptions


@pytest.fixture(autouse=True)
def openBrowser():
    o = EdgeOptions()
    o.add_experimental_option("detach", True)
    # global driver
    driver = Edge(options=o)
    driver.get('https://www.saucedemo.com/')
    driver.maximize_window()
    driver.implicitly_wait(60)
    print('Opening Browser')
    yield driver
    print('Closing Browser')
    driver.close()