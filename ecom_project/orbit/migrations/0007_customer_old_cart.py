# Generated by Django 5.0.7 on 2024-11-11 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orbit', '0006_customer_address1_customer_address2_customer_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='old_cart',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
