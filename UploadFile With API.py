# ===========================================================
# models.py


from django.db import models

class FileUploader(models.Model):
    file_path = models.FileField(upload_to='uploads/')
    format = models.CharField(max_length=10)


# ===========================================================
# serializers.py


from rest_framework import serializers
import os

def validate_file_format(value):
    ext = os.path.splitext(value.name)[1]  # get file format
    valid_extensions = ['.mp4', '.jpg', '.png']  # valid format
    if not ext.lower() in valid_extensions:
        raise serializers.ValidationError("فرمت فایل معتبر نیست. فقط فرمت‌های mp4، jpg و png مجاز هستند.")

class FileSerializer(serializers.Serializer):
    file = serializers.FileField(
        max_length=None,
        allow_empty_file=False,
        validators=[validate_file_format],
    )


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


from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .serializers import FileSerializer
from .models import FileUploader
from django.utils.crypto import get_random_string
import os

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