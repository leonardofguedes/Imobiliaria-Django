from django import forms
from rental.models import Imovel


class AuthorImovelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        fields = 'title', 'description', 'financible', 'category', \
            'area', 'price', 'street', 'city', 'district', \
            'cover', 'photo'