# ===========================================================
# Terminal


python manage.py startapp Log


# ===========================================================
# Create loggers.py file
# Log/loggers.py


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


def saveLog(request):
    try:
        date = getDate()
        time = getTime()
        ip = getIp(request)
        agent = getAgent(request)
        language = getLanguage(request)
        logObject = Logger(date=date, time=time, ip=ip, agent=agent, language=language)
        logObject.save()
    except:
        pass


# ===========================================================
# Log/admin.py


from django.contrib import admin

from django.contrib import admin
from . import models

class showLogs(admin.ModelAdmin):
    list_display = ["ip", "date", "time", "agent", "language"]

admin.site.register(models.Logger, showLogs)


# ===========================================================
