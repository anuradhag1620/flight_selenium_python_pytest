import configparser

#config is object
config = configparser.RawConfigParser()
config.read("/Users/toad/Documents/selenium_python_pytest/Configurations/config.ini")

class ReadConfig:
    #static method can be accessed directly without creating object
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getbrowser():
        browser = config.get('common info', 'browser')
        return browser

    @staticmethod
    def getdriverpath():
        chromedriverpath = config.get('common info', 'chromeDriverPath')
        return chromedriverpath