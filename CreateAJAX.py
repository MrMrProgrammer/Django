# ===========================================================
# pay attentions !


# add this link on html page

    # <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>


# ===========================================================
# index.html


# <p id="data"></p>
# <button class="btn btn-success" onclick="addDate()" id="save-date-btn">ثبت تاریخ</button>


# ===========================================================
# script.js


function addDate() {

    var data = document.getElementById("data").value;

    $.get('/order/add-data?data=' + data).then(res => {
        console.log('ok');
    });
}


# ===========================================================
# views.py


def getData(request):
    data = request.GET.get('data')

    return Response


# ===========================================================