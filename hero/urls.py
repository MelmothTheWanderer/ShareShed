
from django.contrib import admin 
from django.urls import path 
  
#import the view from hero.views
from .views import hero_display
  
urlpatterns = [ 
    path('', hero_display ), 
] 