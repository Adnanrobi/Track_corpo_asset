from django.shortcuts import render, get_object_or_404
from .models import Device

def device_list(request):
    devices = Device.objects.all()
    return render(request, 'devices/device_list.html', {'devices': devices})

def device_detail(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    return render(request, 'devices/device_detail.html', {'device': device})

# Example view for device checkout
def device_checkout(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    if request.method == 'POST':
        # Logic to process device check-out here
        pass
    return render(request, 'devices/device_checkout.html', {'device': device})