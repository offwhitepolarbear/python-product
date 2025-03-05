from django.db import models


class Coupon(models.Model):
    # 쿠폰 코드 (문자열, 고유값)
    code = models.CharField(unique=True, max_length=100)
    # 쿠폰 할인율 (소수점) 별도의 이야기가 없어 
    # product 할인율과 동일한 배율, 자릿수 적용
    discount_rate = models.DecimalField(max_digits=3, decimal_places=2)
