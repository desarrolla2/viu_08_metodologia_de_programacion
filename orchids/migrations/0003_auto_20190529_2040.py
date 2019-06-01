# Generated by Django 2.2.1 on 2019-05-29 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orchids', '0002_auto_20190529_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='greenhouse',
            name='temperature',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orchid',
            name='max_temperature',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orchid',
            name='min_temperature',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='greenhouse',
            name='weather',
            field=models.CharField(choices=[('andes', 'andes'), ('coast', 'coast')], default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='orchid',
            name='weather',
            field=models.CharField(choices=[('andes', 'andes'), ('coast', 'coast')], default='', max_length=200),
        ),
    ]