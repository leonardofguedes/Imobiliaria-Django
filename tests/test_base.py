from django.test import TestCase
from rental.models import Category, Imovel
from django.contrib.auth.models import User


class RentalTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def make_category(self, name='Category'):
        return Category.objects.create(name=name)

    def make_author(self,
                    first_name='user',
                    last_name='name',
                    username='username',
                    password='123456',
                    email='user@gmail.com',):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
        )

    def make_imovel(self,
                    category_data=None,
                    author_data=None,
                    title='Test Title',
                    description='Descript Test',
                    slug='test-slug',
                    financible='Sim',
                    area=50,
                    price=50000,
                    street='Rua das Algas',
                    district='Centro',
                    city='Porto Velho',
                    is_published=True):
        if category_data == None:
            category_data = {}

        if author_data == None:
            author_data = {}

        return Imovel.objects.create(
            category=self.make_category(**category_data),
            author=self.make_author(**author_data),
            title=title,
            description=description,
            slug=slug,
            financible=financible,
            area=area,
            price=price,
            street=street,
            district=district,
            city=city,
            is_published=is_published,
        )
