# Generated by Django 5.1.4 on 2024-12-24 10:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_users_rent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='Rent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.goods'),
        ),
    ]