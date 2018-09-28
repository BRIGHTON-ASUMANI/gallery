from django.db import models
import datetime as dt

# Create your models here.

class Location(models.Model):
    loc_name = models.CharField(max_length =30)


    def __str__(self):
        return self.loc_name

class Category(models.Model):
    cat_name = models.CharField(max_length =30)

    def __str__(self):
        return self.loc_name



class Image(models.Model):
    image = models.ImageField(upload_to = 'articles/')
    image_name = models.CharField(max_length =30)
    image_description = models.TextField()
    category = models.ManyToManyField(Category)
    image_location = models.ForeignKey(Location)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name

    class Meta:
        ordering = ['pub_date']
