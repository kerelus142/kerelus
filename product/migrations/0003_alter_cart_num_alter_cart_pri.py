# Generated by Django 4.0.4 on 2022-05-22 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='num',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='cart',
            name='pri',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
