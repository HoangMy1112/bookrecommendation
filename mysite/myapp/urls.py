
from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name='index'),

    #controller for the details (name=detail)
    path('product/<int:id>', views.detail, name = 'detail'),

    #connect views with the template(create_product.html)
    path("createproduct/", views.create_product, name='createproduct'),

    path("editproduct/<int:id>", views.product_edit, name='editproduct'),

    path("delete/<int:id>", views.product_delete, name='delete'),

    path("dashboard", views.dashboard, name='dashboard'),

    path("register", views.register, name='register'),
]