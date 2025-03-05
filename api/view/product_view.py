import django_filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

from api.serializer.product_serializer import ProductDTOSerializer
from api.service.product_service import ProductService


class ProductFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name="category__name", lookup_expr='iexact')


class ProductSerializer:
    pass


class ProductView(viewsets.ViewSet):
    def __init__(self, product_service=None, **kwargs):
        super().__init__(**kwargs)
        self.product_service = product_service or ProductService()

    def get_product_list(self, request):
        category = request.GET.get('category')  # 카테고리 값 받기
        products = self.product_service.list_all_products(category)
        product_data = [ProductDTOSerializer(product).data for product in products]
        return Response(product_data, status=status.HTTP_200_OK)

    def get_product_detail(self, request, id):
        product = self.product_service.get_product_by_product_id(product_id=id)
        serializer = ProductDTOSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
