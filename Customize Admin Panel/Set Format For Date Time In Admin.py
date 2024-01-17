# ===========================================================
# app/admin.py


class showContactUs(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "message", "formatted_datetime", 'ip']

    def formatted_datetime(self, obj):
        return obj.datetime.strftime('%H:%M | %Y-%m-%d')

admin.site.register(models.ContactUs, showContactUs)


# ===========================================================