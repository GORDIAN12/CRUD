# Generated by Django 5.1.4 on 2024-12-07 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='NOMBRE')),
                ('curp', models.CharField(max_length=100, verbose_name='CURP')),
                ('telefono', models.CharField(max_length=20, verbose_name='NUMERO CELULAR')),
            ],
        ),
    ]
