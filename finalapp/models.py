from django.contrib.auth.models import User
from django.db import models

class Catagory(models.Model):
    catagoryname = models.CharField(max_length=30)
    image = models.ImageField(upload_to='image',default='null.jpg')
    def __str__(self):
        return self.catagoryname

class Product(models.Model):
    mg = models.ImageField(upload_to='image',default='null.jpg')
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    discription = models.CharField(max_length=50)
    stock = models.IntegerField()
    catagory = models.ForeignKey(Catagory,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Cart_User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user

class Cart(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(Cart_User,on_delete=models.CASCADE)
    def total(self):
        return self.quantity*self.product.price

    def __str__(self):
        return self.product.name


class Billing(models.Model):
    country = models.CharField(max_length=20,null=True)
    first_name = models.CharField(max_length=30,default=" ")
    last_name = models.CharField(max_length=30,default=" ")
    address = models.CharField(max_length=50,default=" ")
    state = models.CharField(max_length=20,default=" ")
    postal = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    sub_total = models.IntegerField(default=1)


class Item_order(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    order = models.ForeignKey(Billing, on_delete=models.CASCADE)













