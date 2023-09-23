# ===========================================================
# Tutorial Reference

# URL : https://velog.io/@sjp5554/Validate-Uploaded-File-Size-and-Type-in-Django

# ===========================================================
# validators.py

import magic
from django.utils.deconstruct import deconstructible
from django.template.defaultfilters import filesizeformat


@deconstructible
class FileValidator(object):
    error_messages = {
     'max_size': ("Ensure this file size is not greater than %(max_size)s."
                  " Your file size is %(size)s."),
     'min_size': ("Ensure this file size is not less than %(min_size)s. "
                  "Your file size is %(size)s."),
     'content_type': "Files of type %(content_type)s are not supported.",
    }

    def __init__(self, max_size=None, min_size=None, content_types=()):
        self.max_size = max_size
        self.min_size = min_size
        self.content_types = content_types

    def __call__(self, data):
        if self.max_size is not None and data.size > self.max_size:
            params = {
                'max_size': filesizeformat(self.max_size), 
                'size': filesizeformat(data.size),
            }
            raise ValidationError(self.error_messages['max_size'],
                                   'max_size', params)

        if self.min_size is not None and data.size < self.min_size:
            params = {
                'min_size': filesizeformat(self.min_size),
                'size': filesizeformat(data.size)
            }
            raise ValidationError(self.error_messages['min_size'], 
                                   'min_size', params)

        if self.content_types:
            content_type = magic.from_buffer(data.read(), mime=True)
            data.seek(0)

            if content_type not in self.content_types:
                params = { 'content_type': content_type }
                raise ValidationError(self.error_messages['content_type'],
                                   'content_type', params)

    def __eq__(self, other):
        return (
            isinstance(other, FileValidator) and
            self.max_size == other.max_size and
            self.min_size == other.min_size and
            self.content_types == other.content_types
        )
    

# ===========================================================
# serializers.py

from rest_framework import serializers
from .validators import FileValidator

# In the line below, we enter the types of acceptable formats.
validate_file = FileValidator(max_size=1024 * 100, content_types=('image/png', 'image/jpeg', 'video/mp4'))


# text/plain:
# این Content-Type برای متن ساده (Text) بدون قالب‌بندی خاص مورد استفاده قرار می‌گیرد.

# text/html:
# برای صفحات وب HTML استفاده می‌شود.

# application/json:
# این Content-Type برای داده‌های JSON (JavaScript Object Notation) استفاده می‌شود.

# application/xml:
# این Content-Type برای داده‌های XML (eXtensible Markup Language) استفاده می‌شود.

# application/pdf:
# برای فایل‌های PDF (Portable Document Format) استفاده می‌شود.

# image/jpeg و image/png:
# این Content-Types برای تصاویر JPEG و PNG به ترتیب استفاده می‌شوند.

# audio/mpeg و audio/wav:
# برای فایل‌های صوتی MP3 و WAV به ترتیب استفاده می‌شوند.

# video/mp4 و video/quicktime:
# برای ویدیوهای MP4 و QuickTime به ترتیب استفاده می‌شوند.

# multipart/form-data:
# این Content-Type برای فرم‌های وبی استفاده می‌شود که فایل‌ها را از طریق HTTP POST ارسال می‌کنند. این مورد بسیار معمول در آپلود فایل‌ها به سرور استفاده می‌شود.

# application/x-www-form-urlencoded:
# این Content-Type نیز برای ارسال داده‌ها از طریق فرم‌های وبی استفاده می‌شود. اما در این حالت، داده‌ها به صورت کدنویسی URL (URL-encoded) ارسال می‌شوند.


class FileSerializer(serializers.Serializer):
    file = serializers.FileField(
        max_length=None,
        allow_empty_file=False,
        validators=[validate_file],
    )


# ===========================================================
# models.py


from django.db import models

class FileUploader(models.Model):
    file_path = models.FileField(upload_to='uploads/')
    format = models.CharField(max_length=50)


# ===========================================================
# urls.py


from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'upload', views.FileUploadViewSet, basename='upload')

urlpatterns = [
    path('', include(router.urls)),
]


# ===========================================================
# views.py


import os
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .serializers import FileSerializer
from django.utils.crypto import get_random_string
from .models import FileUploader


class FileUploadViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer_class = FileSerializer(data=request.data)
        if 'file' not in request.FILES or not serializer_class.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            handle_uploaded_file(request.FILES['file'])
            return Response(status=status.HTTP_201_CREATED)

def handle_uploaded_file(f):
    upload_path = 'files'
    os.makedirs(upload_path, exist_ok=True)
    format = os.path.splitext(f.name)[1].lstrip('.')
    random_name = get_random_string(8)
    file_ext = f.name.split('.')[-1]
    new_filename = f"{random_name}.{file_ext}"
    file_path = os.path.join(upload_path, new_filename)
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    file = FileUploader(file_path=file_path, format=format)
    file.save()


# ===========================================================