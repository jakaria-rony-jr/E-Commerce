from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    category_name = models.CharField(max_length=100, blank=True, null=True)
    img = models.ImageField(upload_to='CategoryImg', blank=True, null=True)

    def __str__(self):
        return self.category_name




class Products(models.Model):
    product_name = models.CharField(max_length=100)
    categoris = models.ForeignKey( ProductCategory, verbose_name='Product Cetegory', on_delete=models.CASCADE )
    image = models.ImageField(upload_to='ProductImg/')
    price = models.IntegerField()
    discount_price = models.IntegerField(blank=True, null=True)
    product_purchase_price = models.CharField(max_length=100, blank=True, null=True)
    sort_description = models.CharField(max_length=300,blank=True, null=True)
    description = models.CharField(max_length=300)
    aditional_discription = models.CharField(max_length=300, blank=True, null=True)
    stok_quantity = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.product_name



class FeaturedProducts(models.Model):
    product_name = models.CharField(max_length=100)
    categoris = models.ForeignKey( ProductCategory, verbose_name='Product Cetegory', on_delete=models.CASCADE )
    image = models.ImageField(upload_to='ProductImg/')
    price = models.IntegerField()
    discount_price = models.IntegerField(blank=True, null=True)
    product_purchase_price = models.CharField(max_length=100, blank=True, null=True)
    sort_description = models.CharField(max_length=300,blank=True, null=True)
    description = models.CharField(max_length=300)
    aditional_discription = models.CharField(max_length=300, blank=True, null=True)
    stok_quantity = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'Featured Products'

    def __str__(self):
        return self.product_name



class Banner(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='BannerImg/')
    description = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Big Banner'

    def __str__(self):
        return self.name


class SectionBanner(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='SectionBannerImg/')
    short_description = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Section Banner'

    def __str__(self):
        return self.name


class BestSeller(models.Model):
    product_name = models.CharField(max_length=100)
    categoris = models.ForeignKey( ProductCategory, verbose_name='Product Cetegory', on_delete=models.CASCADE )
    image = models.ImageField(upload_to='BestSellerImg/')
    price = models.IntegerField()
    discount_price = models.IntegerField(blank=True, null=True)
    product_purchase_price = models.CharField(max_length=100, blank=True, null=True)
    sort_description = models.CharField(max_length=300,blank=True, null=True)
    description = models.CharField(max_length=300)
    aditional_discription = models.CharField(max_length=300, blank=True, null=True)
    stok_quantity = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'Best Seller'

    def __str__(self):
        return self.product_name


class Featured(models.Model):
    product_name = models.CharField(max_length=100)
    categoris = models.ForeignKey( ProductCategory, verbose_name='Product Cetegory', on_delete=models.CASCADE )
    image = models.ImageField(upload_to='FeaturedImg/')
    price = models.IntegerField()
    discount_price = models.IntegerField(blank=True, null=True)
    product_purchase_price = models.CharField(max_length=100, blank=True, null=True)
    sort_description = models.CharField(max_length=300,blank=True, null=True)
    description = models.CharField(max_length=300)
    aditional_discription = models.CharField(max_length=300, blank=True, null=True)
    stok_quantity = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'Featured'

    def __str__(self):
        return self.product_name
    

class SpecialOffer(models.Model):
    product_name = models.CharField(max_length=100)
    categoris = models.ForeignKey( ProductCategory, verbose_name='Product Cetegory', on_delete=models.CASCADE )
    image = models.ImageField(upload_to='SpecialOfferImg/')
    price = models.IntegerField()
    discount_price = models.IntegerField(blank=True, null=True)
    product_purchase_price = models.CharField(max_length=100, blank=True, null=True)
    sort_description = models.CharField(max_length=300,blank=True, null=True)
    description = models.CharField(max_length=300)
    aditional_discription = models.CharField(max_length=300, blank=True, null=True)
    stok_quantity = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'Special Offer'

    def __str__(self):
        return self.product_name



class LastBanner(models.Model):
    collection_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='LastBannerImg/')
    sell_offer = models.CharField(max_length=150)
    trends = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Last Banner'

    def __str__(self):
        return self.collection_name
    


class OurClient(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='OurClientImg/')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = 'Our Client'

    def __str__(self):
        return self.name
    

class Services(models.Model):
    services_name = models.CharField(max_length=100)
    services_description = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.services_name














