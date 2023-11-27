# urls.py
from django.urls import path
from .views import index, ExampleApiView

urlpatterns = [
    path('', index, name='index'),
    
]
