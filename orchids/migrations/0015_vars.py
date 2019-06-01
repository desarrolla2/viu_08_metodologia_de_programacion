# Generated by Django 2.2.1 on 2019-06-01 13:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orchids', '0014_auto_20190601_1314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=6, unique=True)),
                ('value', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5000)])),
            ],
        ),
    ]
