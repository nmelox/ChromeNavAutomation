from selenium.webdriver.common.by import By
from appium import webdriver


class Terms:
    """"elements = {
        "acceptButton": (By.ID, "com.android.chrome:id/terms_accept"),
        "sendReportCheck": (By.ID, "com.android.chrome:id/send_report_checkbox"),
        "TermsAndConditions": (By.ID, "com.android.chrome:id/tos_and_privacy")
    }"""""
    acceptButton = (By.ID, "com.android.chrome:id/terms_accept")
    sendReportCheck = (By.ID, "com.android.chrome:id/send_report_checkbox")
    TermsAndConditions = (By.ID, "com.android.chrome:id/tos_and_privacy")

    def __init__(self, driver):
        """self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.elements)"""
        self.driver = driver

    def __clickAcceptButton__(self):
        """self.driver.find_element(self.acceptButton).click()"""
        self.driver.find_element_by_id("com.android.chrome:id/terms_accept").click()

    def __checkSendReport__(self):
        self.driver.find_element(self.sendReportCheck).click()

    def __clickTermsAndConditions__(self):
        self.driver.find_element(self.TermsAndConditions).click()
