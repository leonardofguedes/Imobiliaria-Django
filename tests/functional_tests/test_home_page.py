from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from utils.browser import make_chrome_browser
import time
from selenium.webdriver.common.by import By


class HomePageFunctionalTest(StaticLiveServerTestCase):
    def sleep(self, seconds=5):
        """Apenas para que dê tempo e possamos ver o teste sendo feito no browser"""
        time.sleep(seconds)

    def test_the_test(self):
        browser = make_chrome_browser()
        browser.get(self.live_server_url)
        self.sleep(6)
        body = browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('Nenhum imóvel cadastrado ainda', body.text)
        browser.quit()
