from selenium.webdriver.common.by import By
from .base_test import BaseFunctionalTest
from unittest.mock import patch


class HomePageFunctionalTest(BaseFunctionalTest):
    @patch('rental.views.PER_PAGE', new=2)
    def test_home_page_without_houses_message(self):
        self.make_home_in_batch(qtd=0)
        self.browser.get(self.live_server_url)
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('Nenhum imóvel cadastrado ainda', body.text)
