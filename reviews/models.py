from django.db import models
from uincom.models import Product
from django.utils.timezone import now
# Create your models here.

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(default=now)


class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=1)  # 1 to 5 scale
    created_at = models.DateTimeField(default=now)
