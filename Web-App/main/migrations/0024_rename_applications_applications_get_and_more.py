# Generated by Django 5.0.1 on 2025-01-11 15:51

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_alter_goods_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Applications',
            new_name='Applications_get',
        ),
        migrations.AlterModelOptions(
            name='applications_get',
            options={'verbose_name': 'Заявка на получение', 'verbose_name_plural': 'Заявки на получение'},
        ),
        migrations.CreateModel(
            name='Applications_repair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('Comment', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Комментарий')),
                ('Status', models.CharField(choices=[('На рассмотрении', 'На рассмотрении'), ('Выполнено', 'Выполнено'), ('Отказано', 'Отказано')], default='На рассмотрении', max_length=100, verbose_name='Статус заявки')),
                ('Request', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.goods')),
            ],
            options={
                'verbose_name': 'Заявка на ремонт',
                'verbose_name_plural': 'Заявки на ремонт',
            },
        ),
    ]
