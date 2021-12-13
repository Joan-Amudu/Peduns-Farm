from django.db import models


# Create your models here.
class Contact(models.Model):
    """
    User booking model for contact inquiries
    """
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.full_name
