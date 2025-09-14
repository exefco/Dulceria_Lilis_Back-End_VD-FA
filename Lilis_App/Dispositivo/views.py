from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard(request):
    return render(request, "/Lilis_App/Accounts/dashboard.html")

def inicio(request):
    return render(request,"/Lilis_App/Accounts/base.html")