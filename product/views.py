from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def product_index_view(request):
    return render(request, 'product.html')
