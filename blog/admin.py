from django.contrib import admin
from .models import*

@admin.register(BlogTopic)
class BlogTopicAdmin(admin.ModelAdmin):
    list_display=['blogtopic','created']

@admin.register(Archive)
class ArchiveAdmin(admin.ModelAdmin):
    list_display=['month','year']

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display=['blog_topic','blog_post','created','author']#,'image','video']