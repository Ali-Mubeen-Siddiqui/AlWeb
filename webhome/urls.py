from django.urls import path
from webhome import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path("home/",views.index,name="home"),
    
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('reviews/',views.review_page,name='reviews')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)