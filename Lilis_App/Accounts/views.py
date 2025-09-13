from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Device

@login_required
def devices_list(request):
    org = request.user.userprofile.organization
    qs = Device.objects.filter(organization=org).select_related("category", "zone")
    return render(request, "devices/list.html", {"devices": qs})
