from rental import views
from rental.tests.test_base import RentalTestBase
from django.urls import reverse, resolve


class TestDetailPage(RentalTestBase):
    def test_unity_detail_template_loads_correct_unitys(self):
        """Testando se a detail page carrega o template correto"""
        self.make_imovel(title='Detail Page test')
        response = self.client.get(reverse('imoveis-house', kwargs={
            'category_id': 1}
            ))
        content = response.content.decode('utf-8')
        self.assertIn('Detail Page test', content)

    def test_unity_detail_template_if_not_published(self):
        """Testando caso o is_published não seja True na detail page"""
        imovel = self.make_imovel(is_published=False)
        response = self.client.get(reverse('imoveis-house', kwargs={
            'category_id': imovel.category_id}
                            ))
        self.assertEqual(response.status_code, 404)

    def test_detail_view_function_is_correct(self):
        """Testando se o método view correto é carregado"""
        view = resolve(
              reverse('imoveis-house', kwargs={'category_id': 1})
                )
        self.assertIs(view.func, views.imovel)

    def test_detail_view_returns_404_if_no_unity_found(self):
        """Testando o status da página no caso de não existir imóvel cadastrado"""
        response = self.client.get(
                reverse('imoveis-house', kwargs={'category_id': 1000})
                )
        self.assertEqual(response.status_code, 404)

    def test_detail_template_loads_the_correct_home(self):
        """Testando o carregamento do template com um título inserido no teste"""
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

    def test_detail_template_dont_load_home_not_published(self):
        """Testando o status quando o is_published for False"""
        recipe = self.make_imovel(is_published=False)
        response = self.client.get(
            reverse(
            'imoveis-house',
            kwargs={'category_id': recipe.id}))
        self.assertEqual(response.status_code, 404)
