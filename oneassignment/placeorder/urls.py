from django.urls import path
from .views import *

app_name = 'placeorder'
urlpatterns = [
    path('', redirect_to_products),
    path('browse', browse_products)
]