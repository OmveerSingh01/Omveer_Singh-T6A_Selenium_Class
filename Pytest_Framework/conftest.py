import pytest
from selenium import webdriver
from config.env import ConfigReader

@pytest.fixture
def setup_and_teardown():
    # Read Config
    config = ConfigReader.read_config()
    env = config['qa']
    base_url = env["base_url"]
    # setup (Before test )
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(base_url)
    yield driver  # Test runs here
    # Teardown (runs after test)
    driver.quit()
