from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ecommerce_index_view(request):
    '''This function render index page of ecomerce views'''

    return HttpResponse('Welcome to CN334 Pradipat views!')
