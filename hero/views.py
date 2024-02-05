from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hero_display(request):
  return HttpResponse('This will be the hero section of the website')
