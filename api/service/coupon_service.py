from api.dto.coupon_dto import CouponDto
from api.model import Coupon


class CouponService:
    def get_coupon_by_coupon_code(self, coupon_code: str):
        coupon = Coupon.objects.get(code=coupon_code)
        return CouponDto(coupon.id, coupon.code, coupon.discount_rate)

    def get_all_coupon_list(self):
        coupons = Coupon.objects.all()
        return [CouponDto(coupon.id, coupon.code, coupon.discount_rate) for coupon in coupons]
