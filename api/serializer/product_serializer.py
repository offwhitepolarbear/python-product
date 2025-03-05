from rest_framework import serializers


class ProductDTOSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    price = serializers.IntegerField()
    category_name = serializers.CharField(max_length=100)
    discount_rate = serializers.DecimalField(max_digits=3, decimal_places=2)
    discounted_price = serializers.IntegerField()
    coupon_applicable = serializers.BooleanField()
    final_price = serializers.IntegerField()