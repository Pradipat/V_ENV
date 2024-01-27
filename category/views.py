from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def category_index_view(request , item_id):

    context_data = {
        "item_id": item_id   
    }

    return render(request, 'category.html' , context = context_data)


