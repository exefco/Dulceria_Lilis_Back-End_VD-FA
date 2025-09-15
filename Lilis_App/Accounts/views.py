from django.shortcuts import render,redirect
from django.views import View
from .forms import UsuarioForm
from .models import Usuario,Rol
import bcrypt

class Registrarse(View):
    template_name = 'accounts/register.html'
    def get(self,request):
        form = UsuarioForm()
        return render(request, "accounts/register.html", {"form": form})
    
    def post(self,request):
        form = UsuarioForm( request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        return render(request, self.template_name, {"form": form})

class Login(View):
    template_name = 'accounts/login.html'
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):        
        next_url = request.POST.get('next')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            usuario = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            return render(request, self.template_name, {"error": "Email o contraseña incorrectos."})

        if bcrypt.checkpw(password.encode('utf-8'), usuario.password.encode('utf-8')):
            request.session['usuario_id'] = usuario.id
            if next_url:
                return redirect(next_url)
            return redirect('products_dashboard')

        return render(request, self.template_name, {"error": "Email o contraseña incorrectos."})
    
def Logout(request):
    request.session.flush()
    return redirect("login")