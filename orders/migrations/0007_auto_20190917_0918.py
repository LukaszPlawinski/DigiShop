# Generated by Django 2.2.4 on 2019-09-17 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20190917_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
