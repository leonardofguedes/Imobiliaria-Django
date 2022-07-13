from django import forms
from rental.models import Imovel
from .django_forms import add_attr
from collections import defaultdict
from django.core.exceptions import ValidationError
from utils.strings import is_positive_number

class AuthorImovelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._my_errors = defaultdict(list)

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

    def clean(self, *args, **kwargs):
        super_clean = super().clean(*args, **kwargs)
        cd = self.cleaned_data

        title = cd.get('title')
        description = cd.get('description')

        if title == description:
            self._my_errors['title'].append('Cannot be equal to description')
            self._my_errors['description'].append('Cannot be equal to title')

        if self._my_errors:
            raise ValidationError(self._my_errors)

        return super_clean

    def clean_title(self):
        title = self.cleaned_data.get('title')

        if len(title) < 5:
            self._my_errors['title'].append('Must have at least 5 chars.')

        return title

    def clean_area(self):
        field_name = 'area'
        field_value = self.cleaned_data.get(field_name)

        if not is_positive_number(field_value):
            self._my_errors[field_name].append('Must be a positive number')

        return field_value
