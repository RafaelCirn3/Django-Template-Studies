# Generated by Django 5.1 on 2024-08-16 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=8)),
                ('logradouro', models.CharField(blank=True, max_length=255, null=True)),
                ('bairro', models.CharField(blank=True, max_length=255, null=True)),
                ('localidade', models.CharField(blank=True, max_length=255, null=True)),
                ('uf', models.CharField(blank=True, max_length=2, null=True)),
            ],
        ),
    ]
