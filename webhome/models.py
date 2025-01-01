from django.db import models

# Create your models here.
class Gallery(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to='gallery_images/')

    def __str__(self):
        return f"{self.name}   -   {self.date}  -  {self.image}"