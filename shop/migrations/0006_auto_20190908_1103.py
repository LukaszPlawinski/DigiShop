# Generated by Django 2.2.4 on 2019-09-08 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20190908_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.IntegerField(blank='False', default=''),
        ),
    ]