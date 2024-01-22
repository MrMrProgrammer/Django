# ===========================================================
# app/forms.py


from django import forms

class TestForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()


# ===========================================================
# app/views.py
    

def index(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            print(f'Name: {name}, Email: {email}')

            return HttpResponse('It is RESPONSE !')

    form = TestForm()
    context = {
        'form': form,
    }

    return render(request, 'index.html', context)


# ===========================================================
# app/url.py


urlpatterns = [
    path('', views.index, name='index'),
]


# ===========================================================
# template.html


<form id="testForm" action="" method="post">
    {% csrf_token %}
    {{ form.name.label }}<br/>
    {{ form.name }}<br/><br/>
    {{ form.email.label }}<br/>
    {{ form.email }}<br/><br/>
    <button type="button" id="submitBtn" onclick="submitForm()">Submit</button>
</form>


# ===========================================================
# script.js


<script>
    function submitForm() {
        var formData = $("#testForm").serialize();

        $.ajax({
            type: "POST",
            url: "{% url 'index' %}",
            data: formData,
            success: function (response) {
                console.log(response);
            },
            error: function (error) {
                console.log(error);
            }
        });
    }
</script>


# ===========================================================