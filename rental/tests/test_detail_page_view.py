from rental import views
from rental.tests.test_base import RentalTestBase
from django.urls import reverse, resolve


class TestDetailPage(RentalTestBase):
    def test_unity_detail_template_loads_correct_unitys(self):
        #need a imovel for test
        #testando a detail page, que carrega apenas um imóvel
        self.make_imovel(title='Detail Page test')
        response = self.client.get(reverse('imoveis-house', kwargs={
            'category_id':1}
            ))
        content = response.content.decode('utf-8')
        #checando se o imóvel foi inserido
        self.assertIn('Detail Page test', content)

    def test_unity_detail_template_if_not_published(self):
        #testando caso o is_published não seja True na detail page
        #need a imovel for test com o is-pub False
        imovel = self.make_imovel(is_published=False)
        response = self.client.get(reverse('imoveis-house', kwargs={
            'category_id': imovel.category_id}
                            ))
        # Checando se a menssagem do template aparece
        self.assertEqual(response.status_code, 404)


    def test_detail_view_function_is_correct(self):
        view = resolve(
              reverse('imoveis-house', kwargs={'category_id': 1})
                )
        self.assertIs(view.func, views.imovel)

    def test_detail_view_returns_404_if_no_unity_found(self):
        response = self.client.get(
                reverse('imoveis-house', kwargs={'category_id': 1000})
                )
        self.assertEqual(response.status_code, 404)

    def test_detail_template_loads_the_correct_home(self):
        needed_title = 'This is a detail page'
        # Need a recipe for this test
        self.make_imovel(title=needed_title)
        response = self.client.get(
            reverse(
            'imoveis-house',
            kwargs={'category_id': 1}))
        content = response.content.decode('utf-8')
        # Check if one recipe exists
        self.assertIn(needed_title, content)

    def test_detail_template_dont_load_recipe_not_published(self):
        """Test recipe is_published False dont show"""
        # Need a recipe for this test
        recipe = self.make_imovel(is_published=False)
        response = self.client.get(
            reverse(
            'imoveis-house',
            kwargs={'category_id': recipe.id}))
        self.assertEqual(response.status_code, 404)