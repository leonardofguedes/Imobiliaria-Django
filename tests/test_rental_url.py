from django.test import TestCase
from django.urls import reverse, resolve


class RentalURLTest(TestCase): #testando urls
    def test_rental_home_url_is_correct(self):
        home_url = reverse('imobiliaria-home')
        self.assertEqual(home_url, '/')
        #testando se a home é chamada com '/'

    def test_rental_imovel_url_is_correct(self):
        url = reverse('imoveis-house', kwargs={'category_id':1})
        self.assertEqual(url, '/imovel/1/')

    def test_rental_search_url_is_correct(self):
        url = reverse('search')
        self.assertEqual(url, '/imovel/search/')