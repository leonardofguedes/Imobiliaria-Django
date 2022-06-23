from .test_base import RentalTestBase
from django.core.exceptions import ValidationError


class RentalModelTeste(RentalTestBase):
    def setUp(self) -> None:
        self.rental = self.make_imovel()
        return super().setUp()

    def test_imovel_title_if_has_more_than_65_chars(self):
        self.rental.title = 'Titulo'*65

        with self.assertRaises(ValidationError):
            self.rental.full_clean()


