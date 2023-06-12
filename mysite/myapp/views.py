from django.shortcuts import render
#import Product model to shop up the product (models.py)
from .models import Product
# Create your views here.
def index(request):
    products = Product.objects.all() #product contains the list of all product we have
    return render(request, 'myapp/index.html', {'products': products}) #pass it as context to show product in html page