from django.shortcuts import render
from .models import Drink, Flavor


def home(request):
    context = {
        "drinks": Drink.objects.all(),
        "flavors": Flavor.objects.filter(sugar_free=False),
        "sugar_free_flavors": Flavor.objects.filter(sugar_free=True),
    }
    return render(request, "home.html", context)


def gallery(request):
    return render(request, "gallery.html")
