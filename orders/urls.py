from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'slider', SliderDetails, basename='slider'),
router.register(r'coupon', CouponDetails, basename='coupon'),
router.register(r'promotion', PromotionDetails, basename='promotion'),
router.register(r'slider', SliderDetails, basename='slider'),

urlpatterns = [
     path('', include(router.urls)),
     path('place-order/', PLaceOrder.as_view(), name='place-order'),
     path('decline-item/', DeclineItem.as_view(), name='decline-item'),
     path('order-complete/', CompleteOrder.as_view(), name='order-complete'),
]
