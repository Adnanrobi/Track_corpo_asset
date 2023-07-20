from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Device

class DeviceModelTest(TestCase):
    def setUp(self):
        self.device = Device.objects.create(device_type='phone', model='iPhone X', serial_number='12345')

    def test_device_model_str(self):
        self.assertEqual(str(self.device), 'phone - iPhone X (12345)')

class DeviceAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.device_data = {
            'device_type': 'phone',
            'model': 'Galaxy S20',
            'serial_number': '67890',
        }
        self.device = Device.objects.create(**self.device_data)

    def test_device_list(self):
        url = reverse('api-device-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_device_detail(self):
        url = reverse('api-device-detail', args=[self.device.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_device_create(self):
        url = reverse('api-device-list')
        response = self.client.post(url, self.device_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_device_update(self):
        url = reverse('api-device-detail', args=[self.device.id])
        updated_data = {
            'device_type': 'tablet',
            'model': 'iPad Pro',
            'serial_number': '99999',
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.device.refresh_from_db()
        self.assertEqual(self.device.device_type, 'tablet')
        self.assertEqual(self.device.model, 'iPad Pro')
        self.assertEqual(self.device.serial_number, '99999')

    def test_device_delete(self):
        url = reverse('api-device-detail', args=[self.device.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Device.objects.filter(id=self.device.id).exists())