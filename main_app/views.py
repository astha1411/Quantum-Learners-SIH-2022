from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render (request, 'main_app/home.html')
