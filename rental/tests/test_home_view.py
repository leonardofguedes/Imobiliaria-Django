from django.urls import reverse, resolve
from rental import views
from rental.tests.test_base import RentalTestBase
from unittest.mock import patch

class RentalViewTest(RentalTestBase):
    def test_rental_home_view_is_correct(self):
        """Testando se a view correta é carregada em Home"""
        view = resolve(reverse('imobiliaria-home'))
        self.assertIs(view.func, views.home)

    def test_rental_home_shows_no_unity_found_if_no_unity(self):
        """Testando home quando não houver imóveis cadastrados"""
        response = self.client.get(reverse('imobiliaria-home'))
        self.assertIn(
            'Nenhum imóvel cadastrado ainda',
            response.content.decode('utf-8'))

    def test_rental_home_view_returns_status_200_OK(self):
        """Testando o status code quando o cliente utilizar a URL de Home"""
        response = self.client.get(reverse('imobiliaria-home'))
        self.assertEqual(response.status_code, 200)

    def test_rental_home_view_loads_template(self):
        """Testando o template carregado quando o cliente utilizar a URL de Home"""
        response = self.client.get(reverse('imobiliaria-home'))
        self.assertTemplateUsed(response, 'rental/partials/base.html')

    def test_rental_home_template_loads_unitys(self):
        """Testando Home quando houver um Imóvel criado"""
        self.make_imovel()
        response = self.client.get(reverse('imobiliaria-home'))
        content = response.content.decode('utf-8')
        response_context_unitys = response.context['imoveis']
        self.assertIn('Test Title', content)
        self.assertEqual(len(response_context_unitys), 1)

    def test_rental_home_template_not_published(self):
        """Testando Home quando o Imóvel receber is_published = False"""
        self.make_imovel(is_published=False)
        response = self.client.get(reverse('imobiliaria-home'))
        # Checando se a menssagem do template aparece
        self.assertIn(
            '<h1>Nenhum imóvel cadastrado ainda</h1>',
            response.content.decode('utf-8'))

    def test_home_is_paginated_default(self):
        """Testando se a Home recebe paginação Obs: pelo default do PERPAGE são 6 por página"""
        response = self.client.get(reverse('imobiliaria-home'))
        imoveis = response.context['imoveis']
        paginator = imoveis.paginator
        self.assertEqual(paginator.num_pages, 1)

    @patch('rental.views.PER_PAGE', new=9)
    def test_home_is_paginated_defined(self):
        """Testando se a Home recebe paginação com PERPAGE = 9 """
        from rental.views import Imovel
        for i in range(18):
            kwargs = {'author_data':{'username': f'u{i}'}, 'slug': f'r{i}'}
            self.make_imovel(**kwargs)

        response = self.client.get(reverse('imobiliaria-home'))
        imoveis = response.context['imoveis']
        paginator = imoveis.paginator
        self.assertEqual(paginator.num_pages, 2)


    def test_home_first_page_is_paginated_defined(self):
        """Testando se a primeira página de Home recebe 3 imóveis
           Utilizando Patch(PERPAGE = 3) de uma outra maneira"""
        self.make_home_in_batch(qtd=8)

        with patch('rental.views.PER_PAGE', new=3):
            response = self.client.get(reverse('imobiliaria-home'))
            imoveis = response.context['imoveis']
            paginator = imoveis.paginator
            self.assertEqual(len(paginator.get_page(1)), 3)
