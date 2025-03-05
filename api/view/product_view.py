from rest_framework.response import Response
from rest_framework import status, viewsets

from api.serializer.product_serializer import ProductDTOSerializer
from api.service.coupon_service import CouponService
from api.service.product_service import ProductService


class ProductView(viewsets.ViewSet):
    def __init__(self, product_service=None, coupon_service=None, **kwargs):
        super().__init__(**kwargs)
        self.product_service = product_service or ProductService()
        self.coupon_service = coupon_service or CouponService()

    def get_product_list(self, request):
        category = request.GET.get('category')  # 카테고리 값 받기
        products = self.product_service.list_all_products(category)
        product_data = [ProductDTOSerializer(product).data for product in products]
        return Response(product_data, status=status.HTTP_200_OK)

    def get_product_detail(self, request):
        product_id = request.query_params.get('product_id')
        coupon_code = request.query_params.get('coupon_code')
        product = self.product_service.get_product_by_product_id(product_id=product_id)
        if product.coupon_applicable and coupon_code:
            coupon = self.coupon_service.get_coupon_by_coupon_code(coupon_code)
            product = product.get_coupon_final_price(coupon)
        serializer = ProductDTOSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
