from django.db import models
import datetime as dt

# Location model

class Location(models.Model):
    location = models.CharField(max_length =30)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()


# Category model
class Category(models.Model):
    category = models.CharField(max_length =30)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()


# Image model
class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length =30)
    image_description = models.TextField()
    category = models.ManyToManyField(Category)
    location = models.ForeignKey(Location)
    post_date = models.DateTimeField(auto_now_add=True)


    @classmethod
    def get_all(cls):
        image = cls.objects.order_by('post_date')
        return image

    @classmethod
    def search_by_category(cls,search_term):
        pictures = cls.objects.filter(category__category__icontains=search_term)
        return pictures
