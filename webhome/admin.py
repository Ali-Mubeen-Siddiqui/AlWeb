from django.contrib import admin
from .models import *


admin.site.site_header = "Al~Hamd Caterers Admin"
admin.site.site_title = "Al~Hamd Caterers Admin"
admin.site.index_title = "Welcome to Al~Hamd Caterers Admin"



# Register your models here.


admin.site.register(Gallery)
admin.site.register(Book)
admin.site.register(Contact)
admin.site.register(Review)