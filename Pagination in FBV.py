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


# ===========================================================
# template.html


<nav aria-label="Page navigation example">
    <ul class="pagination page-number">

        {% if objects.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ objects.previous_page_number }}" aria-label="Previous">
                    <span aria-hidden="true">&laquo;</span>
                </a>
            </li>

        {% endif %}

        {% for pageNumber in objects.paginator.page_range %}
            <li class="page-item">
                <a class="page-link {% if objects.number == pageNumber %}page_active{% endif %}" href="?page={{ pageNumber }}" {% if objects.number == pageNumber %}style="color: white; background-color: #0a660a" {% endif %}>{{ pageNumber }} </a>
            </li>
        {% endfor %}

        {% if objects.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ objects.next_page_number }}" aria-label="Next">
                    <span aria-hidden="true">&raquo;</span>
                </a>
            </li>
        {% endif %}
    </ul>
</nav>

# ===========================================================