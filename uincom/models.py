from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.URLField(blank=True, null=True)
    source = models.CharField(max_length=50)  # To identify whether it's from TechMart or StyleShop
    
    def __str__(self):
        return f"{self.name} - {self.price},{self.image},{self.source}"
