from django import forms
from rental.models import Imovel
from .django_forms import add_attr


class AuthorImovelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        add_attr(self.fields.get('description'), 'class', 'span-2')

    class Meta:
        model = Imovel
        fields = 'title', 'description', 'financible', 'category', \
            'area', 'price', 'street', 'city', 'district', \
            'cover', 'photo'

    widgets = {
        'cover': forms.FileInput(
            attrs={
                'class': 'span-2'
            }
        ),
    }