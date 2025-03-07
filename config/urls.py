"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from api.view.coupon_view import CouponView
from api.view.product_view import ProductView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', ProductView.as_view({'get': 'get_product_list'}), name='product-list'),  # URL 매핑
    path('product/', ProductView.as_view({'get': 'get_product_detail'}), name='product-detail'),
    path('coupons/', CouponView.as_view({'get': 'get_all_coupon'}), name='coupon-list'),

    # path('api/', include('api.urls')),  # API URL 추가
]

