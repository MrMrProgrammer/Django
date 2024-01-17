# ===========================================================
# app/admin.py


class CustomCssAdminForm(forms.ModelForm):
    class Meta:
        model = models.CustomCss
        fields = '__all__'  # You can also select the desired field
        widgets = {
            'css': forms.Textarea(attrs={'style': 'direction: ltr;'}),
        }

class showCustomCss(admin.ModelAdmin):
    list_display = ["is_active", "css"]

    list_filter = ['is_active']

    form = CustomCssAdminForm

admin.site.register(models.CustomCss, showCustomCss)


# ===========================================================