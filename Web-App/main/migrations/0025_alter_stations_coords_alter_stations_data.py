# Generated by Django 5.0.1 on 2025-03-16 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_alter_stations_options_rename_count_stations_coords_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stations',
            name='coords',
            field=models.CharField(max_length=10000000000, null=True, verbose_name='координаты'),
        ),
        migrations.AlterField(
            model_name='stations',
            name='data',
            field=models.CharField(max_length=10000000000, null=True, verbose_name='карта'),
        ),
    ]
