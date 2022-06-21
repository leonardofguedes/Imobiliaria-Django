from django.urls import reverse, resolve
from rental import views
from tests.test_base import RentalTestBase


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
        response_context_recipes = response.context['imoveis']

    def test_rental_category_view_return_status_code_404_if_no_unity_found(self):
        response = self.client.get(
            reverse('imoveis-house', kwargs={'category_id':1000}))
        self.assertEqual(response.status_code, 404)

    def test_rental_category_view_is_correct(self):
        view = resolve(reverse('imoveis-house', kwargs={'category_id':1000}))
        self.assertIs(view.func, views.imovel)