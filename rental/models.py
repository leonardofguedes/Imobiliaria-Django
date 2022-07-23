from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField
from django.urls import reverse
from django.utils.text import slugify
from tag.models import Tag


class Photo(models.Model):
    main_photo = models.ImageField(null=True, blank=True, upload_to ='imoveis/main_photos/%Y/%m/%d/')
    second_photo = models.ImageField(null=True, blank=True, upload_to ='imoveis/second_photos/%Y/%m/%d/')
    third_photo = models.ImageField(null=True, blank=True, upload_to ='imoveis/third_photos/%Y/%m/%d/')
    fourth_photo = models.ImageField(null=True, blank=True, upload_to='imoveis/fourth_photos/%Y/%m/%d/')

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
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='photos', null=True, blank=True, default='')
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