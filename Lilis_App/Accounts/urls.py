from django.urls import path
from .views import Login,Registrarse, Logout

urlpatterns = [
    path('login/', Login.as_view(template_name='accounts/login.html'), name='login'),
    path('registrarse/', Registrarse.as_view(template_name="accounts/register.html"), name='registrarse'),
    path('logout/', Logout, name='logout'),
]