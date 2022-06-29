from django.test import TestCase
from django.urls import reverse, resolve


class RentalURLTest(TestCase):
    def test_rental_home_url_is_correct(self):
        """Testando se a URL de Home é chamada com o '/'"""
        home_url = reverse('imobiliaria-home')
        self.assertEqual(home_url, '/')

    def test_rental_detail_page_url_is_correct(self):
        """Testando se a URL de um imóvel único é chamada"""
        url = reverse('imoveis-house', kwargs={'category_id':1})
        self.assertEqual(url, '/imovel/1/')

    def test_rental_search_url_is_correct(self):
        """Testando se a URL da search bar é chamada"""
        url = reverse('search')
        self.assertEqual(url, '/imovel/search/')