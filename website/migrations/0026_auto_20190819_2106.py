# Generated by Django 2.2.4 on 2019-08-20 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0025_merge_20190819_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escola',
            name='data_requisicao',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data de requisição'),
        ),
    ]
