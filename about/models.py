from django.db import models
from products.models import Product


# Create your models here.
class About(models.Model):    
    title = models.CharField(max_length=254)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Recommended_products(models.Model):
    product = models.ForeignKey(Product, null=False,
                                blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.product
