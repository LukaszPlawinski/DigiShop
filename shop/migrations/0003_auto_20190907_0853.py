# Generated by Django 2.2.4 on 2019-09-07 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20190901_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(blank='False'),
        ),
    ]
