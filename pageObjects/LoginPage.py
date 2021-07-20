from selenium import webdriver

class LoginPage():

        textbox_username_name = "userName"
        textbox_password_xpath = "//input[@name='password']"
        button_submit_name = "submit"

# Initialize driver so create constructor
# Constructor invokes at the time of object creation
#capture driver from test case, and tat driver will be insitaied to the class variable.
#Action method on the above locators

        def __init__(self, driver):
            self.driver = driver

#Action methods

        def setUserName(self, username):
            self.driver.find_element_by_name(self.textbox_username_name).clear()
            self.driver.find_element_by_name(self.textbox_username_name).send_keys(username)

        def setPassword(self, password):
            self.driver.find_element_by_xpath(self.textbox_password_xpath).clear()
            self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)

        def clicksignin(self):
            self.driver.find_element_by_name(self.button_submit_name).click()





