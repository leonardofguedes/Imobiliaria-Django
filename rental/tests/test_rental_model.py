from .test_base import RentalTestBase, Imovel
from django.core.exceptions import ValidationError
from parameterized import parameterized

class RentalModelTeste(RentalTestBase):
    def setUp(self) -> None:
        self.rental = self.make_imovel()
        return super().setUp()

    def test_imovel_title_if_has_more_than_65_chars(self):
        self.rental.title = 'Titulo'*65
        with self.assertRaises(ValidationError):
            self.rental.full_clean()

    @parameterized.expand([
        ('title', 65),
        ('description', 265),
        ('city', 25),
        ('street', 165),
        ('district', 25),
    ])
    def test_rental_fields_max_lenght(self, field, max_lenght):
        """Metodo averigua varias falhas propositais e levanta erro apenas se nao falhar
           O subtest não funciona com o Pytest de uma forma efetiva.
           Para termos infos precisas sobre qual teste falhou, melhor utilizar:
           $ python manage.py test
        """
        setattr(self.rental, field, 'A' * (max_lenght + 1))
        with self.assertRaises(ValidationError):
            self.rental.full_clean()

    def make_rental_no_default_field(self):
        """Método para ser utilizado em outros testes sem a adição de nenhum campo Default"""
        imovel = Imovel(
            category=self.make_category(name='Test Default Category'),
            author=self.make_author(username='newuser'),
            title='Test Title',
            description='Descript Test',
            slug='test-slug-models',
            financible='Sim',
            area=50,
            price=50000,
            street='Rua das Algas',
            district='Centro',
            city='Porto Velho', )
        imovel.full_clean()
        imovel.save()
        return imovel

    def test_home_is_published_default(self):
        """Teste para confirmar o is_published > default = False"""
        imovel = self.make_rental_no_default_field()
        self.assertFalse(
            imovel.is_published,
            msg='O is_published default é Falso, não podendo ser omitido esse field'
        )

    def test_home_string_representation(self):
        """Testando a representação em String do nome do Animal"""
        needed = 'Testing Representation'
        self.rental.title = 'Testing Representation'
        self.rental.full_clean()
        self.rental.save()
        self.assertEqual(
            str(self.rental), needed,
            msg=f'Animal string representation must be {needed} but'
                f'{str(self.rental)} was received')
