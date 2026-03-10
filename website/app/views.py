from django.shortcuts import render
from .models import Drink, Flavor, Bean


def menu(request):
    context = {
        "hot_drinks": Drink.objects.filter(category="Hot"),
        "cold_drinks": Drink.objects.filter(category="Cold"),
        "flavors": Flavor.objects.filter(sugar_free=False),
        "sugar_free_flavors": Flavor.objects.filter(sugar_free=True),
    }
    return render(request, "menu.html", context)


def beans(request):
    context = {
        "arabica": Bean.objects.filter(category="Arabica"),
        "robusta": Bean.objects.filter(category="Robusta"),
        "single": Bean.objects.filter(category="Single-Origin Coffee"),
    }
    return render(request, "beans.html", context)


def home(request):
    return render(request, "home.html")


def gallery(request):
    return render(request, "gallery.html")
