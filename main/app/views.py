from rest_framework.generics import ListAPIView
from .models import Product, Warehouse
from .serializers import ProductSerializer, WarehouseSerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        name = self.request.query_params.get('name', None)
        if name:
            queryset = queryset.filter(name=name)

        code = self.request.query_params.get('code', None)
        if code:
            queryset = queryset.filter(code=code)

        group = self.request.query_params.get('group', None)
        if group:
            queryset = queryset.filter(group=group)

        warehouse_id = self.request.query_params.get('warehouse', None)
        if warehouse_id:
            queryset = queryset.filter(warehouse__id=warehouse_id)

        return queryset


class WarehouseProductListView(ListAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        warehouse_id = self.request.query_params.get('warehouse', None)
        if warehouse_id:
            queryset = queryset.filter(id=warehouse_id)

        name = self.request.query_params.get('name', None)
        if name:
            queryset = queryset.filter(products__name=name)

        code = self.request.query_params.get('code', None)
        if code:
            queryset = queryset.filter(products__code=code)

        group = self.request.query_params.get('group', None)
        if group:
            queryset = queryset.filter(products__group=group)

        return queryset
