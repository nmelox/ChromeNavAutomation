from Tools.TearDown import TearDown
from Tools.Initialize import Initialize
import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.desired_capabilities = Initialize.setupConnection(self)
        self.driver = Initialize.createDriver(self)

    def test_OpenChrome(self):
        self.testCase = 'OpenChrome'
        self.driver.find_element_by_id("com.android.chrome:id/terms_accept").click()

    def tearDown(self):
        self.teardown = TearDown(self.driver, self.testCase)
        self.teardown.finishTestCase()
