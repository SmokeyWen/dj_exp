# Generated by Django 3.1.1 on 2020-09-04 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='height',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='listing',
            name='initial_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='listing',
            name='width',
            field=models.FloatField(),
        ),
    ]
