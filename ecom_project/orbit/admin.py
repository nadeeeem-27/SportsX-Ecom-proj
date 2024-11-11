from django.contrib import admin
from django.contrib.auth.models import User
from . models import Category,Product,Customer,Order

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)

# mix customer and user
class CustomerInline(admin.StackedInline):
    model=Customer

class Useradmin(admin.ModelAdmin):
    model= User
    field = ["username","first_name","last_name","email"]
    inlines=[CustomerInline]

# unregister your models here.
admin.site.unregister(User)

# register your models here.
admin.site.register(User, Useradmin)