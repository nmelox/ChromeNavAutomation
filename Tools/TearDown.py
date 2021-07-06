import datetime


class TearDown:
    filePath = 'D:\Automation\Appium\Python\ChromeNavigation\Test Cases\Screenshots\TC_'
    fileExtension = '.png'
    fileDate = datetime.datetime.now().strftime("%d-%m-%Y_%H%M%S")

    def __init__(self, driver, testCase):
        self.driver = driver
        self.testCaseName = testCase

    def __takeAScreenshot__(self):
        self.driver.get_screenshot_as_file(self.filePath + self.testCaseName + self.fileDate + self.fileExtension)

    def finishTestCase(self):
        self.__takeAScreenshot__()
        self.driver.quit()
