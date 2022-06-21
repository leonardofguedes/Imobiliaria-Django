from django.urls import reverse, resolve
from rental import views
from django.test import TestCase
from rental.models import Category, Photo, Imovel
from django.contrib.auth.models import User


class RentalViewTest(TestCase):
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
        """testamos se o template da home carregerá imóveis adicionados"""
        category_test = Category.objects.create(name='Category')
        author_test = User.objects.create_user(
            first_name='user',
            last_name='name',
            username='username',
            password='123456',
            email='user@gmail.com'
        )
        imovel = Imovel.objects.create(
            category = category_test,
            author = author_test,
            title= 'Test Title',
            description = 'Descript Test',
            slug = 'test-slug',
            financible = 'Sim',
            area = 50,
            price = 50000,
            street = 'Rua das Algas',
            district = 'Centro',
            city = 'Porto Velho',
            is_published = True,
        )
        response = self.client.get(reverse('imobiliaria-home'))
        content = response.content.decode('utf-8')
        response_context_rental = response.context['imoveis']
        self.assertIn('Test Title', content)
        self.assertIn('50', content)
        self.assertIn('Rua das Algas', content)
        self.assertEqual(len(response_context_rental), 1)
        ...

    def test_rental_category_view_return_status_code_404_if_no_unity_found(self):
        response = self.client.get(
            reverse('imoveis-house', kwargs={'category_id':1000}))
        self.assertEqual(response.status_code, 404)

    def test_rental_category_view_is_correct(self):
        view = resolve(reverse('imoveis-house', kwargs={'category_id':1000}))
        self.assertIs(view.func, views.imovel)