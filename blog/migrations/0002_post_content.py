# Generated by Django 4.2.3 on 2023-10-19 12:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(null=True, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
