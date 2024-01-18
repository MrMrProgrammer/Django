# ===========================================================
# app/admin.py


from django.contrib import admin
from .models import YourModel

class YourModelAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Category 1', {
            'fields': ('field1', 'field2'),
        }),
        ('Category 2', {
            'fields': ('field3', 'field4'),
        }),
        # Add more categories as needed
    )

admin.site.register(YourModel, YourModelAdmin)


# ===========================================================