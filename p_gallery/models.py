from django.db import models
import datetime as dt
import pyperclip
# from cloudinary.models import CloudinaryField
# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='photo/',null=True)
    # image =CloudinaryField('image',null=True)
    image_name=models.CharField(max_length=20)
    image_description=models.TextField()
    image_location=models.ForeignKey('Location',on_delete=models.DO_NOTHING,null=True)
    image_category=models.ForeignKey('Category',on_delete=models.DO_NOTHING,null=True)
    published=models.DateTimeField(auto_now_add=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.save()

    @classmethod
    def get_image_by_id(cls,id):
        image=cls.objects.get(id=id)
        return image

    @classmethod
    def search_image(cls,search_term):
        images=cls.objects.filter(image_category__name__icontains=search_term) 
        return images

    @classmethod
    def copy_image(cls,id):
        image=cls.objects.get(id=id)
        pyperclip.copy(image.image)

    @classmethod
    def location_find(cls,location):
        images=cls.objects.filter(location=location)
        return images

    def __str__(self):
        return self.image_name

class Location(models.Model):
    place= models.CharField(max_length=30,null=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.save()

    def __str__(self):
        return self.place

class Category(models.Model):
    category=models.CharField(max_length=20,null=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.save()

    def __str__(self):
        return self.category