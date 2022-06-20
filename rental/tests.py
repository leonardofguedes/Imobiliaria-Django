from django.test import TestCase
from django.urls import reverse

class RentalURLTest(TestCase):
    def test_rental_home_url_is_correct(self):
        home_url = reverse('imobiliaria-home')
        self.assertEqual(home_url, '/')
        #testando se a home é chamada com '/'

    def test_rental_imovel_url_is_correct(self):
        url = reverse('imoveis-house', kwargs={'category_id':1})
        self.assertEqual(url, '/imovel/1/')
