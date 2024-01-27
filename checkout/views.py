from django.shortcuts import render
from django.http import HttpResponse



def checkout_index_view(request):
    return render(request, 'checkout.html' )

