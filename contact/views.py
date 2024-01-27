from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def contact_index_view(request):
    return render(request, 'contact.html')
