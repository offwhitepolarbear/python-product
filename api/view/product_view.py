import django_filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.service.product_service import ProductService


class ProductFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name="category__name", lookup_expr='iexact')


class ProductView(APIView):
    def __init__(self, product_service=None, **kwargs):
        super().__init__(**kwargs)
        self.product_service = product_service or ProductService()

    def getProductList(self, request):
        category = request.GET.get('category')  # 카테고리 값 받기
        products = self.product_service.list_all_products(category)
        product_data = [product.__dict__ for product in products]
        return Response(product_data, status=status.HTTP_200_OK)

    def getProductDetail(self, request, id):
        product = self.product_service.get_product_dto(product_id=id)
        # serializer = ProductSerializer(product)
        return Response(product, status=status.HTTP_200_OK)
