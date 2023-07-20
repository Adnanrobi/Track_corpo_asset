from django.db import models

class Device(models.Model):
    DEVICE_TYPES = [
        ('phone', 'Phone'),
        ('tablet', 'Tablet'),
        ('laptop', 'Laptop'),
        # Add other types here
    ]

    device_type = models.CharField(choices=DEVICE_TYPES, max_length=10)
    model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=50, unique=True)
    payment_status = models.BooleanField(default=False)  # New field for payment status

    def __str__(self):
        return f"{self.device_type} - {self.model} ({self.serial_number})"