from django.shortcuts import render
from .forms import UsuarioForm
from .models import Usuario,Rol
import bcrypt


def inicio(request):
        return render(request, "accounts/inicio.html")
# Create your views here.
def registrarse(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "accounts/register_success.html")
    else:
        form = UsuarioForm()
    return render(request, "accounts/register.html", {"form": form})


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            usuario = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            return render(request, "accounts/login.html", {"error": "Email o contraseña incorrectos."})
        if bcrypt.checkpw(password.encode('utf-8'), usuario.password.encode('utf-8')):
            return render(request, "accounts/dashboard.html", {"usuario": usuario})
        else:
            return render(request, "accounts/login.html", {"error": "Email o contraseña incorrectos."})
    return render(request, "accounts/login.html")
