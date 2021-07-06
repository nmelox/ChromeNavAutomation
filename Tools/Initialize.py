from appium import webdriver

class Initialize:


    def __init__(self):
        self.desired_capabilities: dict[str, str]
        self.driver = None
    def setupConnection(self):
        self.desired_capabilities = {
            "platformVersion": "10",
            "platformName": "Android",
            "deviceName": "angelica",
            "automationName": "UiAutomator1",
            "appPackage": "com.android.chrome",
            "appActivity": "com.google.android.apps.chrome.Main"
        }
        return self.desired_capabilities

    def createDriver(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_capabilities)
        return self.driver
