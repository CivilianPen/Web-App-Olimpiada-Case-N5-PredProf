# Generated by Django 5.0.1 on 2024-12-21 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_applications_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applications',
            old_name='User',
            new_name='username',
        ),
    ]