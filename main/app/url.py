from django.urls import path

from .views import ProductListView, WarehouseProductListView

urlpatterns = [
    path('products', ProductListView.as_view()),
    path('warehouse-products', WarehouseProductListView.as_view()),
]
