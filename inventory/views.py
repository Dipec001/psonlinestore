from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from .models import InventoryItem, Supplier
from .serializers import InventoryItemSerializer, SupplierSerializer

# Create your views here.

class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

    def partial_update(self, request, *args, **kwargs):
        if not request.data:
            return Response({"detail": "No data provided for update."}, status=status.HTTP_400_BAD_REQUEST)
        
        return super().partial_update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"detail": "Inventory item has been deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    def partial_update(self, request, *args, **kwargs):
        if not request.data:
            return Response({"detail": "No data provided for update."}, status=status.HTTP_400_BAD_REQUEST)
        
        return super().partial_update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"detail": "Supplier has been deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


class ItemSuppliersView(generics.ListAPIView):
    serializer_class = SupplierSerializer

    def get_queryset(self):
        item_id = self.kwargs['item_id']
        return Supplier.objects.filter(items__id=item_id)

class SupplierItemsView(generics.ListAPIView):
    serializer_class = InventoryItemSerializer

    def get_queryset(self):
        supplier_id = self.kwargs['supplier_id']
        return InventoryItem.objects.filter(suppliers__id=supplier_id)
