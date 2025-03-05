import decimal
from decimal import Decimal, ROUND_DOWN


class ProductDTO:
    def __init__(self, id, name, description, price, discount_rate, coupon_applicable, category_name):
        self.final_price = None
        self.id = id
        self.name = name
        self.description = description
        self.price: int = price
        self.discount_rate: Decimal = discount_rate
        self.coupon_applicable = coupon_applicable
        self.category_name = category_name
        self.discounted_price = self.get_discounted_price()

    def get_discounted_price(self):
        discounted_price = Decimal(self.price) * (1 - self.discount_rate)
        # 소수점 이하 버림 처리
        return discounted_price.quantize(Decimal('1'), rounding=ROUND_DOWN)

    def get_coupon_final_price(self, coupon):
        final_price = Decimal(self.discounted_price) * (1 - coupon.discount_rate)
        self.final_price = final_price.quantize(Decimal('1'), rounding=ROUND_DOWN)
        return self
