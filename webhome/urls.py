from django.urls import path
from webhome import views

urlpatterns = [
    path('', views.index, name='home'),
    path("home/",views.index,name="home"),
    
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
]