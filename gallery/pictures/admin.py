from django.contrib import admin
from .models import Image, Category, Location

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('category',)

admin.site.register(Image,ImageAdmin)
admin.site.register(Category)
admin.site.register(Location)
