
from django.urls import path, include
from .import views
from django.contrib.auth import views as auth_view #rename as auth_view
from django.conf.urls.static import static
from django.conf import settings

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

    path("login/", auth_view.LoginView.as_view(template_name='myapp/login.html'), name='login'), #present it into my app

    path("logout/", auth_view.LogoutView.as_view(template_name='myapp/logout.html'), name='logout'),

    path("invalid/", views.invalid, name='invalid'),

    path("product/<int:id>/comment/", views.add_comment, name='comment'),

    path("search", views.searchBook, name='search'),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
