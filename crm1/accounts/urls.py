from django.urls import path
from accounts import views  
from . import views  #from base import views


urlpatterns = [
    path("", views.home, name = "home   "),
    path("products/", views.products),
    path("customer/", views.customer),
]
