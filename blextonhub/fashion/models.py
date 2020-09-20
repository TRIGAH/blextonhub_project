from django.db import models
from django.db.models.signals import pre_save, post_save
from blextonhub.utils import unique_slug_generator
from django.urls import reverse

# Create your models here.
class Fashion (models.Model):
    image       = models.ImageField(upload_to='fashion/', null=True, blank=True )
    title       = models.CharField(max_length=120)
    price       = models.DecimalField(max_digits=6,decimal_places=2,default=39.99)
    description = models.TextField()
    slug        = models.SlugField(blank=True, unique=True)
    timestamp   =models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
       return self.title
