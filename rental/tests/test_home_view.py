from django.urls import reverse, resolve
from rental import views
from rental.tests.test_base import RentalTestBase


class RentalViewTest(RentalTestBase):
    """
    def test_rental_home_views_is_correct(self):
        view = resolve('/')
        self.assertTrue(True)
    """

    def test_rental_home_view_is_correct(self):
        view = resolve(reverse('imobiliaria-home'))
        self.assertIs(view.func, views.home)

    def test_rental_home_shows_no_unity_found_if_no_unity(self):
        #testando home quando não houver imóveis cadastrados
        response = self.client.get(reverse('imobiliaria-home'))
        self.assertIn(
            'Nenhum imóvel cadastrado ainda',
            response.content.decode('utf-8'))

    def test_rental_home_view_returns_status_200_OK(self):
        response = self.client.get(reverse('imobiliaria-home'))
        self.assertEqual(response.status_code, 200)

    def test_rental_home_view_loads_template(self):
        response = self.client.get(reverse('imobiliaria-home'))
        self.assertTemplateUsed(response, 'rental/partials/base.html')

    def test_rental_home_template_loads_unitys(self):
        #need a imovel for test
        self.make_imovel()
        response = self.client.get(reverse('imobiliaria-home'))
        content = response.content.decode('utf-8')
        response_context_unitys = response.context['imoveis']
        self.assertIn('Test Title', content)
        self.assertEqual(len(response_context_unitys), 1)

    def test_rental_home_template_not_published(self):
        #testando caso o is_published não seja True
        #need a imovel for test com o is-pub False
        self.make_imovel(is_published=False)
        response = self.client.get(reverse('imobiliaria-home'))
        # Checando se a menssagem do template aparece
        self.assertIn(
            '<h1>Nenhum imóvel cadastrado ainda</h1>',
            response.content.decode('utf-8'))




