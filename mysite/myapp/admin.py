from django.contrib import admin
from .models import Product
#when you login, you cant see db that you create in models.py
#whenever you create table in db, you have to register model of that inside the admin.py
# Register your models here.

admin.site.register(Product)