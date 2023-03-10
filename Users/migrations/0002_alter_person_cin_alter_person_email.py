# Generated by Django 4.1.5 on 2023-02-03 08:57

import Users.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='cin',
            field=models.CharField(max_length=8, primary_key=True, serialize=False, validators=[django.core.validators.MaxLengthValidator(8), django.core.validators.MinLengthValidator(8)], verbose_name='CIN'),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[Users.models.is_mail_esprit]),
        ),
    ]
