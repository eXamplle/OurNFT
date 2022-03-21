from tabnanny import verbose
# from tkinter import CASCADE
from wsgiref.simple_server import demo_app
from xmlrpc.client import Boolean
from django.db import models
from django.contrib.auth.models import User
import imagehash
from numpy import true_divide
# Create your models here.
DIFF_THRESHOLD = 0.2

def image_path(instance, filename):
    return f'images/{instance.image_hash}.png'

def diff(hash1, hash2):
    q1 = bin(int(hash1,16))[2:]
    q2 = bin(int(hash2,16))[2:]
    hamm_dist = len([1 for i,j in zip(q1,q2) if i!=j])
    print(hamm_dist/len(q1))
    return hamm_dist/len(q1)


class PublicImageManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(visibility=True)

def GetImageHash(image):
    return f'{imagehash.phash(imagehash.Image.open(image))}'

def IsUnique(image_hash):
    query = Image.objects.values_list('image_hash')
    return not [i[0] for i in query if diff(i[0], image_hash) < DIFF_THRESHOLD]

class Image(models.Model):
    datetime = models.DateTimeField(verbose_name="Date", auto_now_add=True)
    image = models.ImageField(upload_to=image_path,verbose_name="Image")
    image_hash = models.CharField(max_length=64,verbose_name="Token", null=False, primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Owner", related_name="images")
    text = models.CharField(max_length=200, verbose_name="Text", null=True, blank=True)
    visibility = models.BooleanField(verbose_name="Visible", null=False)
    secret = models.CharField(max_length=50,verbose_name="Secret", null=False)

    objects = models.Manager()
    public = PublicImageManager()
    

    def save(self, is_creating = True, *args, **kwargs):
        if is_creating:
            print("create image object")
            self.secret = User.objects.make_random_password(length=20)
            self.image_hash = GetImageHash(self.image)
            if IsUnique(self.image_hash):
                self.is_unique = True
                super().save(*args, **kwargs)
            else:
                print("not unique image")
                self.is_unique = False
        else:
            print("change image object")
            super().save(*args, **kwargs)

    class Meta:
        ordering = ["-datetime"]

    def __str__(self):
        return "{}'s post".format(self.owner.__str__())
