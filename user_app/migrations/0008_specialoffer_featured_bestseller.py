# Generated by Django 4.2.6 on 2023-10-20 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0007_delete_singlebanner'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='SpecialOfferImg/')),
                ('price', models.IntegerField()),
                ('discount_price', models.IntegerField(blank=True, null=True)),
                ('product_purchase_price', models.CharField(blank=True, max_length=100, null=True)),
                ('sort_description', models.CharField(blank=True, max_length=300, null=True)),
                ('description', models.CharField(max_length=300)),
                ('aditional_discription', models.CharField(blank=True, max_length=300, null=True)),
                ('stok_quantity', models.PositiveIntegerField()),
                ('categoris', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.productcategory', verbose_name='Product Cetegory')),
            ],
            options={
                'verbose_name_plural': 'Special Offer',
            },
        ),
        migrations.CreateModel(
            name='Featured',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='FeaturedImg/')),
                ('price', models.IntegerField()),
                ('discount_price', models.IntegerField(blank=True, null=True)),
                ('product_purchase_price', models.CharField(blank=True, max_length=100, null=True)),
                ('sort_description', models.CharField(blank=True, max_length=300, null=True)),
                ('description', models.CharField(max_length=300)),
                ('aditional_discription', models.CharField(blank=True, max_length=300, null=True)),
                ('stok_quantity', models.PositiveIntegerField()),
                ('categoris', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.productcategory', verbose_name='Product Cetegory')),
            ],
            options={
                'verbose_name_plural': 'Featured',
            },
        ),
        migrations.CreateModel(
            name='BestSeller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='BestSellerImg/')),
                ('price', models.IntegerField()),
                ('discount_price', models.IntegerField(blank=True, null=True)),
                ('product_purchase_price', models.CharField(blank=True, max_length=100, null=True)),
                ('sort_description', models.CharField(blank=True, max_length=300, null=True)),
                ('description', models.CharField(max_length=300)),
                ('aditional_discription', models.CharField(blank=True, max_length=300, null=True)),
                ('stok_quantity', models.PositiveIntegerField()),
                ('categoris', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.productcategory', verbose_name='Product Cetegory')),
            ],
            options={
                'verbose_name_plural': 'Best Seller',
            },
        ),
    ]
