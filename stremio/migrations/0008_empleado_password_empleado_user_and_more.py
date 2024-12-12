# Generated by Django 5.1.4 on 2024-12-09 22:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stremio', '0007_rename_empleados_empleado'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='password',
            field=models.CharField(default='1234', max_length=100, verbose_name='PASSWORD'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='user',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='USER'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='especialidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stremio.empleado'),
        ),
    ]
