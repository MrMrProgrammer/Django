# ===========================================================
# app/admin.py


class showPost(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'visit', 'show_author', 'formatted_datetime', 'short_description', 'image']

    def formatted_datetime(self, obj):
        return obj.datetime.strftime('%H:%M | %Y-%m-%d')

    def show_author(self, obj):
        return obj.author.get_full_name()
    
    formatted_datetime.short_description = 'تاریخ و زمان عضویت'
    

admin.site.register(Post, showPost)


# ===========================================================