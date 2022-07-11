from selenium.webdriver.common.by import By
from .base_test import BaseFunctionalTest


class HomePageFunctionalTest(BaseFunctionalTest):
    def test_home_page_without_houses_message(self):
        self.browser.get(self.live_server_url)
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('Nenhum imóvel cadastrado ainda', body.text)
