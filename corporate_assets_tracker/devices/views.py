from django.contrib import messages
from django.shortcuts import redirect, render
from django.shortcuts import render, get_object_or_404
from .models import Device

def simulate_payment(request, device_id):
    device = get_object_or_404(Device, id=device_id)

    # Placeholder for payment processing. For demonstration, we'll simulate a successful payment.
    success = True

    if success:
        device.payment_status = True  # Mark the device as paid
        device.save()
        messages.success(request, f"Payment successful for {device.device_type} - {device.model}")
    else:
        messages.error(request, "Payment failed. Please try again.")

    return redirect('device_detail', device_id=device_id)

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