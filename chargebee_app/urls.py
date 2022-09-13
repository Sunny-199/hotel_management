from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from . import views

urlpatterns = [
     path('create_customer', CreateCustomer.as_view(), name="create_customer"),
     path('get_items_price', GetItemPrice.as_view(), name="get_items_price"),
     path('checkout', Checkout.as_view(), name="checkout"),
     # path('retrieve_hostedPage', RetrieveHostedPage.as_view(), name="retrieve_hostedPage"),

]
# if settings.DEBUG:
#      urlpatterns += static(settings.MEDIA_URL,
#                            document_root=settings.MEDIA_ROOT)
