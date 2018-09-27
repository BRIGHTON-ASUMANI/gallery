from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'articles/')
    name = models.CharField(max_length =30)
    description = models.CharField(max_length =30)
    
