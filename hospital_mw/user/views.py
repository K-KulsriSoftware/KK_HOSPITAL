from django.shortcuts import render

# Create your views here.
import json

def index(request):
    # context = { }
    return render(request, 'user/index.html', {})
