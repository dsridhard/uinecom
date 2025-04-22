from django.db import models
from django.utils.timezone import now
from orders.models import Order
# Create your models here.
class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    method = models.CharField(max_length=50, choices=[('Card', 'Card'), ('UPI', 'UPI'), ('COD', 'Cash on Delivery')])
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Failed', 'Failed')])
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(default=now)
    
    def __str__(self):
        return f'Payment for Order #{self.order_id}'
class Transaction(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100, unique=True)
    success = models.BooleanField(default=False)
    response = models.TextField()
    created_at = models.DateTimeField(default=now)
    
    def __str__(self):
        return f'Transaction #{self.transaction_id} for Payment #{self.payment_id}'