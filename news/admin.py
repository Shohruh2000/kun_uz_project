from django.contrib import admin
from .models import Category, Region, News, Tag
# Register your models here.


# admin.site.register(Category)
# admin.site.register(Region)
# admin.site.register(News)
# admin.site.register(Tag)

admin.site.register([Category,Region,News,Tag])
