from django.shortcuts import render
from django.http import HttpResponse #importing http response from settings


# Create your views here.

def home(request):
    return render(request, 'accounts/dashboard.html')

def products(request):
    return HttpResponse("products") # Products page

def customer(request):
    return HttpResponse("customer") # customer profile's page


# accounts
#     templates
#         accounts
#             dashboard.html
#                 profile.html
#                     customer.html
