# Generated by Django 5.0.1 on 2024-12-22 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_applications_status_alter_applications_request_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User', models.CharField(max_length=100)),
            ],
        ),
    ]