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
    user_clothes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="my_clothes")

class Closet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    clothes = models.ManyToManyField(Cloth, related_name="closets")


class Article(models.Model):
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # def comments(self):
    #     # article_id가 self.id인 것을 return해라
    #     return Comment.objects.filter(article_id=self.id)
    # def article_images(self):
    #     return ArticleImages.objects.filter(article_id=self.id)

class Board(models.Model):
    contents = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)

# class Comment(models.Model):
#     # Article 하나가 여러개의 Comment를 갖는다(1:N)
#     contents = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)
#     # on_delete:옵션, CASCADE -> 게시글이 삭제되면 댓글도 삭제되어야함

# class HashTag(models.Model):
#     tag = models.CharField(max_length=16, unique=True)
#     articles = models.ManyToManyField(Article, related_name="tags")