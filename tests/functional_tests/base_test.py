from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from utils.browser import make_chrome_browser
import time
from rental.tests.test_base import RentalMixin


class BaseFunctionalTest(StaticLiveServerTestCase, RentalMixin):
    def setUp(self) -> None:
        self.browser = make_chrome_browser()
        return super().setUp()

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()

    def sleep(self, seconds=5):
        """Apenas para que dê tempo e possamos ver o teste sendo feito no browser"""
        time.sleep(seconds)