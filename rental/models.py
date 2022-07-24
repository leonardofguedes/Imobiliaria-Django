from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField
from django.urls import reverse
from django.utils.text import slugify
from tag.models import Tag


class Imovel(models.Model):
    FINAN = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
        ('Indefinido', 'Não informado')
    )
    CATEGO = (
        ('Apartamento', 'Apartamento'),
        ('Casa', 'Casa'),
        ('Terreno', 'Terreno'),
        ('Cobertura', 'Cobertura'),
        ('Desconhecido', 'Desconhecido'),
    )
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=265)
    slug = models.SlugField(unique=True)
    financible = models.CharField(choices=FINAN, blank=False, null=False, default='U', max_length=15)
    area = models.IntegerField()
    price = MoneyField(
        decimal_places=2,
        default=0,
        default_currency='BRL',
        max_digits=13,
    )
    street = models.CharField(max_length=165)
    district = models.CharField(max_length=25)
    city = models.CharField(max_length=25, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cover = models.ImageField(upload_to='imoveis/covers/%Y/%m/%d/', blank=True, default='')
    mainphoto = models.ImageField(upload_to='imoveis/photos/%Y/%m/%d/', blank=True, default='')
    secondphoto = models.ImageField(upload_to='imoveis/photos/%Y/%m/%d/', blank=True, default='')
    thirdphoto = models.ImageField(upload_to='imoveis/photos/%Y/%m/%d/', blank=True, default='')
    fourthphoto = models.ImageField(upload_to='imoveis/photos/%Y/%m/%d/', blank=True, default='')
    fifphoto = models.ImageField(upload_to='imoveis/photos/%Y/%m/%d/', blank=True, default='')
    sixphoto = models.ImageField(upload_to='imoveis/photos/%Y/%m/%d/', blank=True, default='')
    sevphoto = models.ImageField(upload_to='imoveis/photos/%Y/%m/%d/', blank=True, default='')
    category = models.CharField(choices=CATEGO, blank=False, null=False, default='Desconhecido', max_length=30)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
    tags = models.ManyToManyField(Tag, blank=True, default='') # noqa

    def __str__(self):
        return self.title

    def get_absolute_url(self):
       return reverse('imoveis-house', args=(self.pk,))

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(f'{self.title}+(-{self.district})+(-{self.city}')
            self.slug = slug
        return super().save(*args, **kwargs)

