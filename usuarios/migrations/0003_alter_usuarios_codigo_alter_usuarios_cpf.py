# Generated by Django 4.1.4 on 2022-12-26 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_usuarios_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='codigo',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='cpf',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]