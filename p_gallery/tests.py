
from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.
class ImageTestCase(TestCase):
    
    def setUp(self):
        self.image =Image(image_name='image',image_description='image description',image_location=self.location,image_category=self.category)
        self.image.save_image()


        self.category = Category(category='category')
        self.category.save()

        self.location = Location(location='location')
        self.location.save()

    def tearDown(self):
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()
    
    def test_get_imageby_id(self):
        image=Image.get_image_by_id()
        self.assertTrue(len(image)>0)

    def test_search_image(self):
        term='school'
        results=Image.search_image(term)
        self.assertTrue(len(results)==0)

    def test_copy_image(self):
        image=Image.copy_image(id=1)
        self.assertTrue(len(image)==0)