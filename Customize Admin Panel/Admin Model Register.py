# ===========================================================
# admin.py


from django.contrib import admin
from .app-name import models

class showDay(admin.ModelAdmin):
    list_display = ["__str__"]
    list_filter = ["fields"]
    list_editable = ["fields"]

admin.site.register(models.Days, showDay)


# ===========================================================