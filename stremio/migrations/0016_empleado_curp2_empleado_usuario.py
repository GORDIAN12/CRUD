# Generated by Django 5.1.4 on 2024-12-09 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stremio', '0015_empleado'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='curp2',
            field=models.CharField(default='UNKNOWN', max_length=30, verbose_name='CURP2'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='usuario',
            field=models.CharField(default='UNKNOWN', max_length=30, verbose_name='USUARIO'),
        ),
    ]
