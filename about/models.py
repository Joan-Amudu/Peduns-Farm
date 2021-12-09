from django.db import models


# Create your models here.
class About(models.Model):    
    title = models.CharField(max_length=254)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Recommended_Products(models.Model):    
    name = models.CharField(max_length=254)
    description = models.TextField(blank=True)    
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name
  
   