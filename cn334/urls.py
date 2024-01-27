"""
URL configuration for cn334 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 

from ecommerce import views as ecom_views
from homepage import views as homePage_views
from category import views as category_views
from checkout import views as checkout_views
from contact import views as contact_views
from product import views as product_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("ecommerce/", ecom_views.ecommerce_index_view),
    path("ecommerce/item/<item_id>", ecom_views.item_view),
    path("homepage/", homePage_views.homepage_index_view),
    path("category/<item_id>", category_views.category_index_view),
    path("checkout/", checkout_views.checkout_index_view),
    path("contact/", contact_views.contact_index_view),
    path("product/", product_views.product_index_view),
]
