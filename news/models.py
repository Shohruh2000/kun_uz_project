from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50,unique=True)

    def __str__(self):
        return self.name
class Region(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True)
    content = models.TextField()
    img = models.ImageField(upload_to = 'uploads/% Y/% m/% d/')
    craeted_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, null=True)
    region = models.ForeignKey(Region, on_delete = models.SET_NULL, null=True)
    tag = models.ManyToManyField('Tag')

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name