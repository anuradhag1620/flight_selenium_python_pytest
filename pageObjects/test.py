class LoginPage():
    textbox_username_name = "userName"
    textbox_password_xpath = "//input[@name='password']"
    button_submit_name = "submit"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_name(self.textbox_username_name).clear()
        self.driver.find_element_by_name(self.textbox_username_name).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)

    def clicksignin(self):
        self.driver.find_element_by_name(self.button_submit_name).click()
