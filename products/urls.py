from django.urls import path
from .import views

# Create your urls here.
urlpatterns = [
    path('', views.all_products, name='products'),
]
