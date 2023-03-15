from django.contrib import admin
from .models import Category, Region, News, Tag
# Register your models here.


# admin.site.register(Category)
# admin.site.register(Region)
# admin.site.register(News)
# admin.site.register(Tag)




class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,CategoryAdmin)


class RegionAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Region,RegionAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','slug','craeted_at','category','region']
    prepopulated_fields = {'slug':('title',)}

admin.site.register(News,NewsAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ["name",'slug']
    preserve_filters = {'slug':('name',)}


admin.site.register(Tag,TagAdmin)
