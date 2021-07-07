from Tools.TearDown import TearDown
from Tools.Initialize import Initialize
from App.Chrome.Terms import Terms
import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.desired_capabilities = Initialize.setupConnection(self)
        self.driver = Initialize.createDriver(self)

    def test_OpenChrome(self):
        self.testCase = 'OpenChrome'
        self.terms = Terms(self.driver)
        self.terms.acceptTermsConditions()

    def tearDown(self):
        self.teardown = TearDown(self.driver, self.testCase)
        self.teardown.finishTestCase()
