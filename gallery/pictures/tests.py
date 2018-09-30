from django.test import TestCase
from .models import Category, Location, Image

# Create your tests here.
class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.location= Location(location = 'France')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

    # Testing Save Method
    def test_save_method(self):
        self.location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)

class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.category= Category(category = 'Shepherd')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))

    # Testing Save Method
    def test_save_method(self):
        self.category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.location= Location(location = 'France')
        self.location.save_location()

        self.new_category = Category(category = 'Shepherd')
        self.new_category.save()

    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()

    def test_get_all_images(self):
        imagess = Image.all_images()
        self.assertTrue(len(imagess)==0)
