# Generated by Django 4.0.5 on 2022-07-23 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0005_imovel_pics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imovel',
            name='pics',
        ),
    ]
