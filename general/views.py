from django.shortcuts import render

# Create your views here.
def ecommerce_index_view(request):
    '''This function render index page of ecomerce views'''

    return HttpResponse('Welcome to HomePage')
