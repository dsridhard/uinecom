from django.db import models
from django.utils.timezone import now
# Create your models here
class Customer(models.Model):
    firstname = models.CharField(max_length=255)
    lastname= models.CharField(max_length=255)
    email=models.EmailField(null=False,blank=False)
    mobile=models.IntegerField(blank=False,null=False)
    created_at = models.DateTimeField(default=now)
    def __str__(self):
        return f"{self.firstname},{self.lastname},{self.email},{self.mobile},{self.created_at}"
class Address(models.Model):
   
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='addresses')
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.address_line1}, {self.city}, {self.country}"

class CustomerProfile(models.Model):
    Customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/',null=True, blank=True)
    data_of_birth = models.DateField(null=True, blank=True)
    preference=models.TextField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
         return f"{self.Customer.firstname},{self.Customer.lastname},{self.profile_picture},{self.data_of_birth},{self.preference},{self.created_at}"