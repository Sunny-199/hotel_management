from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()


router.register(r'role', UserRole, basename='role'),
router.register(r'user/edit', UserEdit, basename='register'),

urlpatterns = [
     path(
         'user/login/', MyTokenObtainPairView.as_view(), name='login'
         ),
     # path(
     # 'user/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'
     # ),
     path('flat_token', FlatToken.as_view(), name="flat_token"),
     # path('staff', GetStaff.as_view(), name='staff'),
     path('', include(router.urls)),

]
