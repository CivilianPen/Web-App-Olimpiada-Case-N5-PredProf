# Generated by Django 5.0.1 on 2025-03-16 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_url_adress'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stations',
            options={'verbose_name': 'Карта', 'verbose_name_plural': 'Карты'},
        ),
        migrations.RenameField(
            model_name='stations',
            old_name='count',
            new_name='coords',
        ),
        migrations.RenameField(
            model_name='stations',
            old_name='goods',
            new_name='data',
        ),
        migrations.RemoveField(
            model_name='stations',
            name='rented_count',
        ),
    ]
