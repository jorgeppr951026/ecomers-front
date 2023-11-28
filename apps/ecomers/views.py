from django.http import JsonResponse
from django.views import View

import requests

class ExampleApiView(View):
    def get(self, request, *args, **kwargs):
        data = {'message': 'Hello from the API!'}
        return JsonResponse(data)
    
    
    
# views.py
from django.shortcuts import render

def index(request):
    #data = requests.get("https://ecomers-lg2f.onrender.com").json()
    
    return render(request, 'ecomers/index.html',)
