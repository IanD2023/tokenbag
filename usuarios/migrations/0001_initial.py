# Generated by Django 4.1.4 on 2022-12-24 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, null=True)),
                ('codigo', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=100, null=True)),
                ('loja', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
