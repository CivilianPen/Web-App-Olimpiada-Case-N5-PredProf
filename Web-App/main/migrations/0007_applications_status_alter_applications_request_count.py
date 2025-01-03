# Generated by Django 5.0.1 on 2024-12-22 10:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_applications_request_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='Status',
            field=models.CharField(choices=[('На рассмотрении', 'На рассмотрении'), ('Одобрено', 'Одобрено'), ('Отказано', 'Отказано')], default='На рассмотрении', max_length=100, verbose_name='Статус заявки'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='Request_count',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='count'),
        ),
    ]
