from rest_framework import serializers


class CouponDTOSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    code = serializers.CharField()
    discount_rate = serializers.DecimalField(max_digits=3, decimal_places=2)
