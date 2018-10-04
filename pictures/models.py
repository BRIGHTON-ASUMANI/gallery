from django.db import models
import datetime as dt
from django.core.validators import MaxLengthValidator
# Location model

class Location(models.Model):
    location = models.CharField(max_length =30)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

    #deleting
    def delete_location(self):
        self.delete()


# Category model
class Category(models.Model):
    category = models.CharField(max_length =30)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()

    #deleting
    def delete_category(self):
        self.delete()


class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length =30)
    image_description = models.TextField(validators=[MaxLengthValidator(300)])
    category = models.ManyToManyField(Category)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name


    @classmethod
    def all_images(cls):
        image = cls.objects.order_by('post_date')
        return image

    @classmethod
    def get_image(cls, id):
        image = cls.objects.get(id=id)
        return image

    @classmethod
    def search_by_category(cls,search_term):
        pictures = cls.objects.filter(category__category__icontains=search_term)
        return pictures
