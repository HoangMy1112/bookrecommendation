from django.shortcuts import redirect, render
#import Product model to shop up the product (models.py)
from .models import Product
from .forms import ProductForm, UserRegistrationForm#import class ProductForm in formd.py

# Create your views here.
def index(request):
    products = Product.objects.all() #product contains the list of all product we have
    return render(request, 'myapp/index.html', {'products': products}) #pass it as context to show product in html page

#view details of product
def detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'myapp/detail.html', {'product': product}) #pass the product

def create_product(request): #accept request
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES) #get all the in4 in the form when user hit "POST"
        if product_form.is_valid(): #validate
            #if all is valid, save in4 from product form to db
            new_product = product_form.save(commit=False) 
            new_product.seller  = request.user
            new_product.save()
            return redirect('index')
    product_form = ProductForm() #create an instnace
    
    #create path and pass the instance to here
    # you can call back {{product_form}} in create_product.html
    return render(request, 'myapp/create_product.html', {'product_form': product_form})

def product_edit(request, id):
    product = Product.objects.get(id=id) #get the id of update bool
    if product.seller != request.user:
         return redirect('invalid')
    
    product_form = ProductForm(request.POST or None, request.FILES or None, instance=product) #pass the instance of product
    if product_form.is_valid(): #validate
            #if all is valid, save in4 from product form to db
            new_product = product_form.save() #commit changes to db
            return redirect('index')
    return render(request, 'myapp/product_edit.html', {'product_form': product_form})

def product_delete(request, id):
    product = Product.objects.get(id=id) #get the id of delete book
    if product.seller != request.user:
         return redirect('invalid')
    if request.method == 'POST':
         product.delete()
         return redirect('index')
    return render(request, 'myapp/delete.html', {'product': product}) #pass product as context

def dashboard(request):
     products = Product.objects.all()
     return render(request, 'myapp/dashboard.html', {'products': products})

def register(request):
     if request.method == 'POST':
          user_form = UserRegistrationForm(request.POST)#get data from POST request
          new_user = user_form.save(commit=False) 
          #commit=False means we're not saving final data or not commit all POST data to db
          new_user.set_password(user_form.cleaned_data['password']) #access password field
          new_user.save()
          return redirect('index')
     user_form = UserRegistrationForm()
     return render(request, 'myapp/register.html',{'user_form': user_form}) #pass the form

def invalid(request):
     return render(request, 'myapp/invalid.html')