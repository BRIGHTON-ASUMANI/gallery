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
