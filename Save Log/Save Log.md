# User Visit Log

### Terminal
```markdown
python manage.py startapp Log
```



### Log/models.py

```python
from django.db import models


class Logger(models.Model):
    ip = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    VPW = models.BooleanField(default=False)
    count = models.IntegerField(default=1)
    agent = models.CharField(max_length=500)
    language = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'Log'
        verbose_name = "بازدید"
        verbose_name_plural = "بازدید ها"
```


### Log/loggers.py

```python
from jdatetime import datetime
from .models import Logger


def getTime():
    current_datetime = datetime.now()
    shamsi_datetime = current_datetime.togregorian()
    time = shamsi_datetime.strftime("%H:%M")
    return time


def getDate():
    current_datetime = datetime.now()
    date = current_datetime.strftime("%Y/%m/%d")
    return date


def getIp(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip


def getAgent(request):
    agent = request.META.get('HTTP_USER_AGENT')
    return agent


def getLanguage(request):
    language = request.META.get('HTTP_ACCEPT_LANGUAGE')
    return language


def saveLog(request, VPW=False):

    ip = getIp(request)

    has_visited = Logger.objects.filter(ip__iexact=ip)

    if has_visited:
        obj: Logger = Logger.objects.filter(ip=ip).last()

        obj.date = getDate()
        obj.time = getTime()
        obj.count += 1

        obj.save()

    else:
        date = getDate()
        time = getTime()
        agent = getAgent(request)
        language = getLanguage(request)

        logObject = Logger(date=date, time=time, ip=ip, agent=agent, language=language)

        logObject.save()
```

### Log/admin.py

```python
from django.contrib import admin
from . import models


class showLogs(admin.ModelAdmin):
    list_display = ["ip", "date", "time", "VPW", "count", "agent", "language", "client_name"]
    ordering = ['-date', '-time']


admin.site.register(models.Logger, showLogs)
```



### Target views.py (saveLog)
Put the following code on the target page

```python
from Log.loggers import saveLog

# --------------
saveLog(request)
# --------------
```

---

# Saving information related to personal site viewing by the user

### Log/loggers.py

```python
def SaveVPW(request):

    ip = getIp(request)

    has_visited = Logger.objects.filter(ip__iexact=ip)

    if has_visited:
        obj: Logger = Logger.objects.filter(ip=ip).last()
        obj.VPW = True
        obj.save()

    else:
        saveLog(request, VPS=True)
```


### Log/loggers.py
When the user clicks on the personal site link, They are transferred to this function.

```python
def SaveVPW(request):
    loggers.SaveVPW(request)
    return HttpResponseRedirect("https://mrmrprogrammer.pythonanywhere.com/")
```