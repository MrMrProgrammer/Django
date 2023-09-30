# ===========================================================
# admin.py


from django.contrib import admin
from .DRF-Permissions import models

class showDay(admin.ModelAdmin):
    list_display = ["__str__"]
    list_filter = ["fields"]
    list_editable = ["fields"]
    list_filter = ["fields"]

admin.site.register(models.Days, showDay)


# ===========================================================