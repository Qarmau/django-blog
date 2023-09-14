from django.urls import path,include
from django.contrib import admin
from . import views


urlpatterns = [
    path('',views.index,name='index'),
   
    path("users/", include("django.contrib.auth.urls")),
    path('(?<blogtopic_id>\d+)/$',views.blogtopic,name='blogtopic'),
    path('new_post/(?<blogtopic_id>\d+)/$',views.new_post,name='new_post'),
    path("register/", views.register_request, name="register"),
    path("archives/",views.archives,name='archives'),
  


    
]



