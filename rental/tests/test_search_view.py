from rental import views
from rental.tests.test_base import RentalTestBase
from django.urls import reverse, resolve


class SearchViewTest(RentalTestBase):
    def test_rental_search_uses_correct_view_function(self):
        """Testando se a view de search está correta // TDD"""
        resolved = resolve(reverse('search'))
        self.assertIs(resolved.func.view_class, views.ListViewSearch)

    def test_rental_search_loads_correct_template(self):
        """Testando para conferir se o template de search está sendo carregado"""
        response = self.client.get(reverse('search') + '?q=teste')
        self.assertTemplateUsed(response, 'rental/pages/search.html')

    def test_rental_search_raises_404_if_no_search_term(self):
        """Teste para ver o status code se não houver parâmetro de pesquisa"""
        url = reverse('search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_rental_search_term_is_on_page_title_and_escaped(self):
        """Testando a pesquisa e se o conteúdo escapa"""
        url = reverse('search') + '?q=<Teste>'
        response = self.client.get(url)
        self.assertIn(
            'Procure por &quot;&lt;Teste&gt;&quot;',
            response.content.decode('utf-8')
        )

    def test_rental_search_can_find_unity_by_title(self):
        """Criaremos duas unidades com titulo diferente e buscaremos ambas no search
        No segundo caso, testando a unidade contrária.
        No terceiro caso, testando perante uma queryset vazia.
        """
        title1 = 'This is Home 1'
        title2 = 'This is Home 2'
        unity1 = self.make_imovel(
            slug='one',
            title=title1,
            author_data={'username':'one'}
        )
        unity2 = self.make_imovel(
            slug='two',
            title=title2,
            author_data={'username': 'two'}
        )
        search_url = reverse('search')
        response1 = self.client.get(f'{search_url}?q={title1}')
        response2 = self.client.get(f'{search_url}?q={title2}')
        response_both = self.client.get(f'{search_url}?q=this')
        self.assertIn(
            unity1,
            response1.context['imoveis']
        )
        self.assertNotIn(unity2, response1.context['imoveis'])
        self.assertNotIn(response_both, response1.context['imoveis'])
        self.assertNotIn(response_both, response1.context['imoveis'])