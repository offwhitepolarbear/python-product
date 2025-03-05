from django.db import models


class Category(models.Model):
    # 카테고리 이름 (문자열, 최대 100자)
    name = models.CharField(max_length=100)