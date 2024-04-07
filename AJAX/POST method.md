# Sending form using the ```POST``` method in AJAX


### forms.py

```python
from django import forms

class TestForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
```


### url.py

```python
urlpatterns = [
    path('POST', views.index, name='index'),
]
```


### views.py

```python    
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
```


### template.html

```HTML
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
```

```HTML
<form id="testForm" action="" method="post">
    {% csrf_token %}
    {{ form.name.label }}<br/>
    {{ form.name }}<br/><br/>
    {{ form.email.label }}<br/>
    {{ form.email }}<br/><br/>
    <button type="button" id="submitBtn" onclick="submitForm()">Submit</button>
</form>
```


### script.js

```JavaScript
<script>
    function submitForm() {
        var formData = $("#testForm").serialize();

        $.ajax({
            type: "POST",

            url: "{% url 'index' %}",
            // url: "/POST",

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
```