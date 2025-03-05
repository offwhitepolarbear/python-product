from django.db import models

from api.model.category import Category


class Product(models.Model):
    # 상품 이름 (문자열, 최대 255자)
    name = models.CharField(max_length=255)
    # 상품 설명 (텍스트)
    description = models.TextField()
    # 상품 가격 (정수형, 기본 단위는 원)
    price = models.IntegerField()
    
    # 상품 카테고리 (외래키, Category 모델과 연결)
    # 카테고리 삭제시 방지 처리
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    # 할인율 (소수점, 예: 0.10은 10% 할인) 연산시 주의
    discount_rate = models.DecimalField(max_digits=3, decimal_places=2)

    # 쿠폰 적용 가능 여부 (boolean)
    coupon_applicable = models.BooleanField(default=False)
    