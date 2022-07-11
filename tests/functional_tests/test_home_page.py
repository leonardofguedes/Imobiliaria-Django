from selenium.webdriver.common.by import By
from .base_test import BaseFunctionalTest
from unittest.mock import patch
from selenium.webdriver.common.keys import Keys


class HomePageFunctionalTest(BaseFunctionalTest):
    def test_home_page_without_houses_message(self):
        self.make_home_in_batch(qtd=0)
        self.browser.get(self.live_server_url)
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('Nenhum imóvel cadastrado ainda', body.text)

    @patch('rental.views.PER_PAGE', new=2)
    def test_search_input_can_find_correct_home(self):
        homes = self.make_home_in_batch()

        title_needed = 'This is what I need'

        homes[0].title = title_needed
        homes[0].save()

        # Usuário abre a página
        self.browser.get(self.live_server_url)

        # Vê um campo de busca com o texto "Procure por um imóvel"
        search_input = self.browser.find_element(
            By.XPATH,
            '//input[@placeholder="Procure por um imóvel"]'
        )

        # Clica neste input e digita o termo de busca
        # para encontrar a receita o título desejado
        search_input.send_keys(title_needed)
        search_input.send_keys(Keys.ENTER)

        # O usuário vê o que estava procurando na página
        self.assertIn(
            title_needed,
            self.browser.find_element(By.CLASS_NAME, 'main-content-list').text,
        )

    @patch('rental.views.PER_PAGE', new=2)
    def test_home_page_pagination(self):
        homes = self.make_home_in_batch()

        #User abre a página
        self.browser.get(self.live_server_url)

        #Veja se há paginação e clica na página 2
        page2 = self.browser.find_element(
            By.XPATH,
            '//a[@aria-label="Go to page 2"]'
        )
        page2.click()

        # Averigua se existem mais 2 imóveis na página 2
        self.assertEqual(
            len(self.browser.find_elements(By.CLASS_NAME, 'imovel')),
            2
        )