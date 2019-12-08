from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill, Thumbnail

# Create your models here.

class Category(models.Model):
    cate_id = models.IntegerField()
    cate_name = models.CharField(max_length=16)

class Month(models.Model):
    month = models.IntegerField()

class Temp(models.Model):
    temp = models.IntegerField()

class Cloth(models.Model):
    product_id = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cloth_type = models.CharField(max_length=16)
    color = models.CharField(max_length=16)
    pattern = models.CharField(max_length=16)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    temp = models.ForeignKey(Temp, on_delete=models.CASCADE)
    # label = models.ImageField(blank=True)
    label = models.CharField(max_length=16)
    img_url = models.CharField(max_length=300)

class Closet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    clothes = models.ManyToManyField(Cloth, related_name="closets")

