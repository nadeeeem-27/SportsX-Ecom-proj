# Generated by Django 5.0.7 on 2024-10-18 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orbit', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/product/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/product/'),
        ),
    ]
