# ===========================================================

# pip install django-imagekit

# ===========================================================

# Add 'imagekit' to your INSTALLED_APPS list in your project’s settings.py

# ===========================================================
# app/models.py


from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class YourModel(models.Model):
    image = models.ImageField(upload_to='images/')
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(100, 100)],
                                     format='JPEG',
                                     options={'quality': 60})
    

# =========================================================== 
# app/admin.py
    

from django.contrib import admin
from .models import YourModel

class YourModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_thumbnail_display']

    def image_thumbnail_display(self, obj):
        return mark_safe(f'<img src="{obj.image_thumbnail.url}" width="50" height="50" />')

admin.site.register(YourModel, YourModelAdmin)


# =========================================================== 

# NOTE : Do not forget the settings related to the display of media files.

# https://github.com/MrMrProgrammer/Django/blob/main/Serve%20File.py

# =========================================================== 