# Generated by Django 5.0.1 on 2025-01-11 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_purchaseplan_options_alter_supplier_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='applications',
            options={'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявки'},
        ),
        migrations.AlterModelOptions(
            name='goods',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
