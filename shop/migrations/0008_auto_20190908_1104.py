# Generated by Django 2.2.4 on 2019-09-08 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20190908_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.IntegerField(blank=True, default=''),
        ),
    ]
