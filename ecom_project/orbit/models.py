from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    date_modified = models.DateTimeField(User,auto_now=True)
    phone=models.CharField(max_length=10,blank=True)
    address1=models.CharField(max_length=200,blank=True)
    address2=models.CharField(max_length=200,blank=True)
    city=models.CharField(max_length=200,blank=True)
    state=models.CharField(max_length=200,blank=True)
    zipcode=models.CharField(max_length=200,blank=True)
    country=models.CharField(max_length=200,blank=True)
    old_cart=models.CharField(max_length=2000,blank=True,null=True)


    def __str__(self):
        return self.user.username
    
# create a customer model automatically when user register
def create_customer(sender,instance,created,**kwargs):
    if created:
        user_profile=Customer(user=instance)
        user_profile.save()

# automate the customer thing
post_save.connect(create_customer,sender=User)

# products
class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.DecimalField(default=0,decimal_places=2,max_digits=6)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description=models.CharField(max_length=1500,default='',blank=True,null=True)
    image=models.ImageField(upload_to='uploads/product/') 
    image2=models.ImageField(upload_to='uploads/product/',blank=True, null=True)
    image3=models.ImageField(upload_to='uploads/product/',blank=True, null=True)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    address=models.CharField(max_length=100,default='')
    phone=models.CharField(max_length=10,default='')
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.product

    
