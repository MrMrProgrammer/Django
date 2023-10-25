# ===========================================================
# Settings.py


MEDIA_URL = '/photos/'


# ===========================================================
# urls.py


from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# ===========================================================
# views.py


from django.views.generic import CreateView, ListView

class 'class name' (ListView):
    template_name = 'template address'
    model = 'model name'
    context_object_name = 'files'


# ===========================================================
# template


{% for file in files %}

    <img src="{{ file.image.url }}" />

{% endfor %}


# ===========================================================
