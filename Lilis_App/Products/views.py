from django.shortcuts import render,redirect
from django.views import View
from Accounts.models import Usuario
class Dashboard(View):
    login_url = '/login/'
    template_name = 'products/dashboard.html'
    def get(self,request):
        usuario = None
        usuario_id = request.session.get('usuario_id')
        if usuario_id:
            try:
                usuario = Usuario.objects.get(id=usuario_id)
            except:
                usuario = None
        if not usuario:
            return redirect(f'/login/?next={request.path}')

        return render(request, "products/dashboard.html", {"usuario": usuario})
    
    def post(self,request):
        pass