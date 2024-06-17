from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InventoryItemViewSet, SupplierViewSet, ItemSuppliersView, SupplierItemsView

router = DefaultRouter()
router.register(r'inventory', InventoryItemViewSet)
router.register(r'suppliers', SupplierViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('inventory/<int:item_id>/suppliers/', ItemSuppliersView.as_view(), name='item-suppliers'),
    path('suppliers/<int:supplier_id>/items/', SupplierItemsView.as_view(), name='supplier-items'),
]
