from django.shortcuts import render
from django.views import generic
from .models import Item

# Create your views here.

class ItemList(generic.ListView):
    queryset = Item.objects.filter(in_stock=True)
    template_name = "items_list.html"
    paginate_by = 6

    class Meta:
        ordering = ["-template_name"]