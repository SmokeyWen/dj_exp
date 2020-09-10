# Generated by Django 3.1.1 on 2020-09-08 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20200904_1551'),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='listing_id',
        ),
        migrations.AlterField(
            model_name='comment',
            name='listing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='listings.listing'),
        ),
    ]