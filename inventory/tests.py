from django.test import TestCase
from rest_framework.test import APIClient
from .models import InventoryItem, Supplier
from rest_framework import status
# Create your tests here.


class InventoryAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        self.supplier = Supplier.objects.create(name='Test Supplier', contact_info='08100000000')
        self.inventory_item = InventoryItem.objects.create(name='Test Item', description='Test Description', price='10.00')
        self.inventory_item.suppliers.add(self.supplier)
        self.item_data = {
            'name': 'Test Item',
            'description': 'Test Description',
            'price': '10.00',
            'suppliers': [self.supplier.id]
        }

    def test_create_inventory_item(self):
        initial_count = InventoryItem.objects.count()
        
        response = self.client.post('/api/inventory/', self.item_data, format='json')
        print(response.data)  # Print response data for debugging
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(InventoryItem.objects.count(), initial_count +1)

    def test_get_inventory(self):
        response = self.client.get('/api/inventory/')
        self.assertEqual(response.status_code, 200)

    def test_update_inventory_item(self):
        updated_data = {'name': 'Updated Item Name'}
        response = self.client.patch(f'/api/inventory/{self.inventory_item.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.inventory_item.refresh_from_db()
        self.assertEqual(self.inventory_item.name, 'Updated Item Name')

    def test_delete_inventory_item(self):
        response = self.client.delete(f'/api/inventory/{self.inventory_item.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(InventoryItem.objects.filter(id=self.inventory_item.id).exists())

    def test_list_suppliers_for_item(self):
        response = self.client.get(f'/api/inventory/{self.inventory_item.id}/suppliers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)



class SupplierTests(TestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.supplier_data = {
            'name': 'Test Supplier',
            'contact_info': '08100000000',
        }
        self.supplier = Supplier.objects.create(name='Test Supplier', contact_info='08100000000')
        self.inventory_item = InventoryItem.objects.create(name='Test Item', description='Test Description', price='10.00')
        self.supplier.items.add(self.inventory_item)
    
    def test_create_supplier(self):
        initial_count = InventoryItem.objects.count()
        response = self.client.post('/api/suppliers/', self.supplier_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Supplier.objects.count(), initial_count +1)

    def test_get_suppliers(self):
        response = self.client.get('/api/suppliers/')
        self.assertEqual(response.status_code, 200)
    
    def test_update_supplier(self):
        updated_data = {'name': 'Updated Supplier Name'}
        response = self.client.patch(f'/api/suppliers/{self.supplier.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.supplier.refresh_from_db()
        self.assertEqual(self.supplier.name, 'Updated Supplier Name')
    
    def test_delete_supplier(self):
        response = self.client.delete(f'/api/suppliers/{self.supplier.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Supplier.objects.filter(id=self.supplier.id).exists())
    
    def test_list_items_for_supplier(self):
        response = self.client.get(f'/api/suppliers/{self.supplier.id}/items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
