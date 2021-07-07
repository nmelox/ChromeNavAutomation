from selenium.webdriver.common.by import By


class Terms:
    acceptButton = {"locator": By.ID, "value": "com.android.chrome:id/terms_accept"}
    sendReportCheck = {"locator": By.ID, "value": "com.android.chrome:id/send_report_checkbox"}
    termsAndConditions = {"locator": By.ID, "value": "com.android.chrome:id/tos_and_privacy"}
    nextButton = {"locator": By.ID, "value": "com.android.chrome:id/next_button"}
    yesButton = {"locator": By.ID, "value": "com.android.chrome:id/positive_button"}
    waitActivity = "com.android.chrome:id/search_box_text"

    def __init__(self, driver):
        self.driver = driver

    def __clickAcceptButton__(self):
        self.driver.find_element(self.acceptButton.get("locator"), self.acceptButton.get("value")).click()

    def __checkSendReport__(self):
        self.driver.find_element(self.sendReportCheck.get("locator"), self.sendReportCheck.get("value")).click()

    def __clickTermsAndConditions__(self):
        self.driver.find_element(self.termsAndConditions.get("locator"), self.termsAndConditions.get("value")).click()

    def __clickNextButton__(self):
        self.driver.find_element(self.nextButton.get("locator"), self.nextButton.get("value")).click()

    def __clickYesButton__(self):
        self.driver.find_element(self.yesButton.get("locator"), self.yesButton.get("value")).click()

    def acceptTermsConditions(self):
        self.__clickAcceptButton__()
        self.__clickNextButton__()
        self.__clickYesButton__()
        self.driver.wait_activity(self.waitActivity, 2)
