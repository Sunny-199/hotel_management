from rest_framework import serializers
from .models import *
from main_app.serializers import MenuGetSerializer, HotelSerializer, ItemsGetSerializer
from datetime import datetime


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        validated_data['is_accepted'] = True
        validated_data['accepted_at'] = datetime.now()
        return Order.objects.create(**validated_data)


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = '__all__'

    def create(self, validated_data):
        return OrderItem.objects.create(**validated_data)


class CouponSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coupon
        fields = '__all__'


class PromotionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Promotions
        fields = '__all__'


class SliderSerializerGet(serializers.ModelSerializer):
    menu = MenuGetSerializer(read_only=True)
    promotion = PromotionSerializer(read_only=True)
    hotel = HotelSerializer(read_only=True)
    items = ItemsGetSerializer(read_only=True)

    class Meta:
        model = Slider
        fields = '__all__'


class SliderSerializerEdit(serializers.ModelSerializer):

    class Meta:
        model = Slider
        fields = '__all__'