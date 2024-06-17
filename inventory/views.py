from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from .models import InventoryItem, Supplier
from .serializers import InventoryItemSerializer, SupplierSerializer

# Create your views here.

class InventoryItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing Inventory Items.

    This viewset provides CRUD (Create, Retrieve, Update, Delete) operations
    for Inventory Items.
    """
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

    def partial_update(self, request, *args, **kwargs):
        """
        Performs a partial update of an Inventory Item.

        This method allows updating specific fields of an Inventory Item
        without requiring the entire object data. It checks for empty request data
        and returns a 400 Bad Request response if no data is provided.
        """
        if not request.data:
            return Response({"detail": "No data provided for update."}, status=status.HTTP_400_BAD_REQUEST)
        
        return super().partial_update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        """
        Deletes an Inventory Item.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"detail": "Inventory item has been deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

class SupplierViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing Suppliers.

    This viewset provides CRUD (Create, Retrieve, Update, Delete) operations
    for Suppliers.
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    def partial_update(self, request, *args, **kwargs):
        """
        
        Performs a partial update of a Supplier.

        This method allows updating specific fields of a Supplier
        without requiring the entire object data. It checks for empty request data
        and returns a 400 Bad Request response if no data is provided.
        """
        if not request.data:
            return Response({"detail": "No data provided for update."}, status=status.HTTP_400_BAD_REQUEST)
        
        return super().partial_update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        """

        Deletes a Supplier and returns a message to inform of success.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"detail": "Supplier has been deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


class ItemSuppliersView(generics.ListAPIView):
    """
    API endpoint to retrieve Suppliers for a specific Inventory Item.

    This view retrieves a list of Suppliers associated with a particular
    Inventory Item identified by its ID in the URL.
    """
    serializer_class = SupplierSerializer

    def get_queryset(self):
        item_id = self.kwargs['item_id']
        return Supplier.objects.filter(items__id=item_id)

class SupplierItemsView(generics.ListAPIView):
    """
    APi endpoint to get all inventory items that belong to a particular supplier identified by it's ID in the URL
    """
    serializer_class = InventoryItemSerializer

    def get_queryset(self):
        supplier_id = self.kwargs['supplier_id']
        return InventoryItem.objects.filter(suppliers__id=supplier_id)
