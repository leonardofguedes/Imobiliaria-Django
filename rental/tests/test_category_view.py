from rental import views
from rental.tests.test_base import RentalTestBase
from django.urls import reverse, resolve

class CategoryViewTest(RentalTestBase):
    def test_rental_category_view_return_status_code_404_if_no_unity_found(self):
        response = self.client.get(
            reverse('imoveis-house', kwargs={'category_id':1000}))
        self.assertEqual(response.status_code, 404)

    def test_rental_category_view_is_correct(self):
        view = resolve(reverse('imoveis-house', kwargs={'category_id':1000}))
        self.assertIs(view.func, views.imovel)

    def test_unity_category_template_loads_unitys(self):
        #need a imovel for test
        #testando a category do imóvel
        self.make_imovel(title='Category test')
        response = self.client.get(reverse('imoveis-house', args=(1,)))
        content = response.content.decode('utf-8')
        #checando se o imóvel foi inserido
        self.assertIn('Category test', content)