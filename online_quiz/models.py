from django.db import models
from django.contrib.auth.models import User
from PIL import Image

subjects = (("Eng", "English"), ("Math", "Maths"), ("Programing", "Programming"), ("Comp", "Computer"))


class Test(models.Model):
    category = models.CharField(max_length=64, choices=subjects,default=None)
    question = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255)
    option_4 = models.CharField(max_length=255)
    answer = models.CharField(max_length=255, default=None)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f' { self.user } Profile'

    def save(self, **kwargs):
        super().save()

        img = Image.open( self.image.path )

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)