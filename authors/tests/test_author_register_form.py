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
    def test_fields_placeholder(self, field, placeholder):
        form = RegisterForm()
        current_placeholder = form[field].field.widget.attrs['placeholder']
        self.assertEqual(current_placeholder, placeholder)

    @parameterized.expand([
        ('username', (
                'Required. 150 characters or fewer. '
                'Letters, digits and @/./+/-/_ only.')),
        ('email', 'The e-mail must be valid.'),
        ('password', (
                'Password must have at least one uppercase letter, '
                'one lowercase letter and one number. The length should be '
                'at least 8 characters.'
        )),
    ])
    def test_field_help_test(self, field, needed):
        form = RegisterForm()
        current = form[field].field.help_text
        self.assertEqual(current, needed)
