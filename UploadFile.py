# ===========================================================
# Settings.py

MEDIA_ROOT = BASE_DIR / 'uploads'


# ===========================================================
# forms.py


from django import forms

class Form(forms.Form):
    image = forms.ImageField()


# ===========================================================
# models.py


from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images')


# ===========================================================
# views.py


from django.shortcuts import render
from .forms import Form
from django.views import View
from .models import Image

class form(View):

    def get(self, request):
        form = Form()
        return render(request, 'app/index.html', {'form': form})

    def post(self, request):

        submitted_form = Form(request.POST, request.FILES)

        if submitted_form.is_valid():
            profile = Image(image=request.FILES['image'])
            profile.save()
            return render(request, "app/index.html")

        return render(request, 'app/index.html',{'form': submitted_form})


# ===========================================================
# index.html
# Pay attention to the enctype value in the form !


<form action="#" method="post" enctype="multipart/form-data">
    {% csrf_token %}
    <input type="file" name="image">
    <button type="submit">Submit</button>
</form>


# ===========================================================