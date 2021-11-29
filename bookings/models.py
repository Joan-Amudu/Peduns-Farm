from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserBooking(models.Model):
    """
    User booking model for managing fruit picking bookings
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)    
    number_of_people = models.CharField(max_length=20, null=False, blank=False)
    date = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.user.username
