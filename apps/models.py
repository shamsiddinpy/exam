from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='product/image')
    text = models.TextField()
