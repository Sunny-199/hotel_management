from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'feedback', FeedbackDetails, basename='feedback'),
router.register(r'smily', SmilyDetails, basename='smily'),


urlpatterns = [
     path('', include(router.urls)),
]
