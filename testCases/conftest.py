import selenium
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from utilities.readProperties import ReadConfig


@pytest.fixture()
def setup():
    browser = ReadConfig.getbrowser()
    chromedriverpath = ReadConfig.getdriverpath()
    if browser == 'chrome':
        driver = selenium.webdriver.Chrome(executable_path=chromedriverpath)
    else:
        print("No Chrome")
    return driver
