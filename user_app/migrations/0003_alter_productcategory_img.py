# Generated by Django 4.2.6 on 2023-10-18 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_remove_products_hover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='CategoryImg'),
        ),
    ]
