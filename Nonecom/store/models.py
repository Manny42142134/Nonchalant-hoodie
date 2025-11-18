from django.db import models

class Category(models.Model):
    # from "class category = foreignkey / name = models.Charfild(max_le ... "
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Meta:
    verbose_name_plural = 'categories'



class Customer(models.Model):
    # from "first name / last name / phone / email / password"
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # placeholder field

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Size(models.Model):
    SIZES = [('S','S'), ('M','M'), ('L','L'), ('XL','XL'), ('XXL','XXL'), ('3XL','3XL')]
    name = models.CharField(max_length=4, choices=SIZES, unique=True)

    def __str__(self):
        return self.name
    
class Products(models.Model):
     SIZE_CHOICES = [
        ("S", "S"),
        ("M", "M"),
        ("XL", "XL"),
        ("XXL", "XXL"),
    ]
     name = models.CharField(max_length=200)
     price = models.DecimalField(max_digits=10, decimal_places=2)
     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
     description = models.TextField(blank=True)
     image = models.ImageField(upload_to="products/", blank=True, null=True)
     image_back  = models.ImageField(upload_to="products/", blank=True, null=True)
     size = models.CharField(max_length=4, choices=SIZE_CHOICES, default="S")
     on_sale = models.BooleanField(default=False)
     sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
     sizes = models.ManyToManyField(Size, blank=True, related_name='products')


     def __str__(self):
        return self.name


class Order(models.Model):
    # from "product / customer / quantity integerfield / address / phone number /
    # date datefield / status = Boolean field"
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="orders")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    quantity = models.IntegerField(default=1)
    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    date = models.DateField(auto_now_add=True)  # captures order date automatically
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.id}"


class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100, default="Nonchalant")
    logo = models.ImageField(upload_to="site/", blank=True, null=True) 
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Site Settings"

    class Meta:
        verbose_name_plural = "Site Settings"