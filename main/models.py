from django.db import models
from django.contrib.auth.models import User


class Ads(models.Model):
    img = models.ImageField(upload_to='ads/')

class Region(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField()
    banner_img = models.ImageField(upload_to='post-baner/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='post-img/')


class PostVideo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    video = models.FileField(upload_to='post-video/')
    video_url = models.URLField(blank=True, null=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)