from authors.forms import RegisterForm
from django.test import TestCase
from parameterized import parameterized


class AuthorRegisterFormUnitTest(TestCase):
    @parameterized.expand([
        ('username', 'Seu username'),
        ('email', 'Seu e-mail'),
        ('first_name', 'Ex.: João'),
        ('last_name', 'Ex.: Silva'),
        ('password', 'Digite sua senha'),
        ('password2', 'Repita a senha'),
    ])
    def test_first_name_placeholder_is_correct(self, field, placeholder):
        form = RegisterForm()
        current_placeholder = form[field].field.widget.attrs['placeholder']
        self.assertEqual(current_placeholder, placeholder)