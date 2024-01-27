from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage_index_view(request):
    return render(request, 'homepage.html')
