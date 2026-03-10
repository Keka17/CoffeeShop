from django.core.validators import RegexValidator
from django.db import models


class Drink(models.Model):

    DRINKS_CATEGORIES = [("Hot", "Hot"), ("Cold", "Cold")]

    validator = RegexValidator(
        regex=r"^\d+(\.\d{1,2})?,\d+(\.\d{1,2})?,\d+(\.\d{1,2})?$",
        message="Type three numbers separated by commas without spaces",
    )

    name = models.CharField(max_length=50)
    category = models.CharField(max_length=4, choices=DRINKS_CATEGORIES)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to="drinks/", default="default_drink.jpg")
    prices = models.CharField(
        max_length=30, validators=[validator], help_text="Example: 3.50,4.50,5.50"
    )

    def get_prices(self):
        return self.prices.split(",")


class Flavor(models.Model):
    name = models.CharField(max_length=50)
    sugar_free = models.BooleanField(default=False)


class Bean(models.Model):
    BEAN_TYPES = [
        ("Arabica", "Arabica"),
        ("Robusta", "Robusta"),
        ("Single-Origin Coffee", "Single-Origin Coffee"),
    ]
    ROAST_LEVELS = [("Light", "Light"), ("Medium", "Medium"), ("Dark", "Dark")]

    name = models.CharField(max_length=100)
    category = models.CharField(choices=BEAN_TYPES)
    image = models.ImageField(upload_to="beans/", default="default_bean.jpg")
    country = models.CharField(max_length=30)
    roast = models.CharField(choices=ROAST_LEVELS, default="Medium")
    flavor_notes = models.CharField(max_length=100)
