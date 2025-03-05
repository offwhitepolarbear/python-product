from rest_framework import viewsets, status
from rest_framework.response import Response

from api.serializer.coupon_serailizer import CouponDTOSerializer
from api.service.coupon_service import CouponService


class CouponView(viewsets.ViewSet):
    def __init__(self, coupon_service=None, **kwargs):
        super().__init__(**kwargs)
        self.coupon_service = coupon_service or CouponService()

    def get_all_coupon(self, request):
        coupons = self.coupon_service.get_all_coupon_list()

        coupon_data = [CouponDTOSerializer(coupon).data for coupon in coupons]
        return Response(coupon_data, status=status.HTTP_200_OK)
