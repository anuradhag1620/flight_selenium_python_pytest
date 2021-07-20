from pageObjects.LoginPage import LoginPage
from utilities import XLUtils
from utilities import XLUtils
from utilities.readProperties import ReadConfig


class Test_001_login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData//LoginData.xlsx"

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.username = XLUtils.readData(self.path, 'Sheet1', 2, 1)
        self.password = XLUtils.readData(self.path, 'Sheet1', 2, 2)
        print(self.username, self.password)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicksignin()