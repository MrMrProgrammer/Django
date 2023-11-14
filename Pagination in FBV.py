# ===========================================================
# views.py

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def function_name(request):

    objects = Model.objects.all()

    per_page = 10
    paginator = Paginator(objects, per_page)

    page = request.GET.get('page')

    try:
        ads = paginator.page(page)
    except PageNotAnInteger:
        ads = paginator.page(1)
    except EmptyPage:
        ads = paginator.page(paginator.num_pages)

    context = {
        'objects': ads,
    }

    return render(request, '', context)