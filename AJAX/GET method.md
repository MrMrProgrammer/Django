# Sending data using the ```GET``` method in AJAX


### index.html
```HTML
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
```

```HTML
<p id="data">This is TEST text !</p>

<button type="button" onclick="sendData()">send data</button>
```

### script.js


```JS
function sendData() {

    var text = document.getElementById("data").innerText;
    var number = 12345;

    data = {
        text: text,
        new: number
    }

    $.get('/GET', data).then(res => {
        console.log('ok');
    });
}
```

### views.py

```PYTHON
def getData(request):

    data = request.GET.get('data')

    return Response
```