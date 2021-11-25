from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserBooking(models.Model):
    """
    User booking model for managing fruit picking bookings
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_full_name = models.CharField(max_length=50, null=False, blank=False)
    default_email = models.EmailField(max_length=254, null=False, blank=False)
    default_number_of_people = models.CharField(max_length=20, null=False, blank=False)
    default_phone_number = models.CharField(max_length=20, null=False, blank=False)
    default_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
