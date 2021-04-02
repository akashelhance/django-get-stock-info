
from django.urls import path
from .views import home, about, addstock, deleteStock

urlpatterns = [
    
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('add_stock/', addstock, name="addstock"),
    path('delete/<int:pk>', deleteStock, name="deletestock")
]
