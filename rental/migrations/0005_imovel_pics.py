# Generated by Django 4.0.5 on 2022-07-23 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0004_alter_imovel_category_delete_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='imovel',
            name='pics',
            field=models.FileField(blank=True, default='', upload_to='imoveis/images/%Y/%m/%d/'),
        ),
    ]
