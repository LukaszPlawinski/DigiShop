# Generated by Django 2.2.4 on 2019-09-11 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20190911_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='feature1',
            field=models.CharField(default='Feature', max_length=60),
        ),
        migrations.AlterField(
            model_name='product',
            name='feature2',
            field=models.CharField(default='Feature', max_length=60),
        ),
        migrations.AlterField(
            model_name='product',
            name='feature3',
            field=models.CharField(default='Feature', max_length=60),
        ),
        migrations.AlterField(
            model_name='product',
            name='feature4',
            field=models.CharField(default='Feature', max_length=60),
        ),
        migrations.AlterField(
            model_name='product',
            name='feature5',
            field=models.CharField(default='Feature', max_length=60),
        ),
    ]