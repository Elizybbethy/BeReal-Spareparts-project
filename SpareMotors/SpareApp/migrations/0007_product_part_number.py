# Generated by Django 4.2.4 on 2023-08-24 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SpareApp', '0006_alter_product_arrival_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='part_number',
            field=models.IntegerField(default=0),
        ),
    ]
