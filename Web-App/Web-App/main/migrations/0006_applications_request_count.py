# Generated by Django 5.0.1 on 2024-12-22 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_applications_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='Request_count',
            field=models.IntegerField(default=0, verbose_name='count'),
        ),
    ]
