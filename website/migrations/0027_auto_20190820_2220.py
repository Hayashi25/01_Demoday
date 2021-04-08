# Generated by Django 2.2.4 on 2019-08-21 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_auto_20190819_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escola',
            name='email',
            field=models.EmailField(error_messages={'unique': 'Já existe!'}, max_length=255, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='escola',
            name='nome_escola',
            field=models.CharField(error_messages={'unique': 'Já existe!'}, max_length=255, unique=True, verbose_name='Nome da Escola'),
        ),
    ]