

from django.contrib import admin
from django.urls import path
from ShopApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('Gallery', views.images,name='gallery'),
    path('About', views.about,name='about'),


]
