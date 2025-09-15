from django.urls import path
from .views import Dashboard

urlpatterns = [
    path('dashboard/', Dashboard.as_view(template_name='products/dashboard.html'), name='products_dashboard'),
]