from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def hero_display(request):
  current_year = datetime.date.today().year
  return render(request, "index.html", {
    "current_year" : current_year
  })
