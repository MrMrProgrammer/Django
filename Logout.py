# ===========================================================
# Views.py


from django.contrib.auth import logout

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponse('loged out !')


# ===========================================================
