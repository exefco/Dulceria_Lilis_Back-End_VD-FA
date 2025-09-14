from Dispositivo.views import dashboard

urlpatterns = [
        path("", dashboard, name="dashboard"),
]
