# Generated by Django 5.0.6 on 2024-05-27 13:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthUserManager', '0002_alter_customeuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator(message='Invalid email address')]),
        ),
    ]
