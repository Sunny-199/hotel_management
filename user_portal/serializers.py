from rest_framework import serializers
from main_app.serializers import HotelSerializer
from .models import Feedback, Smily


class FeedbackEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = '__all__'


class SmilyEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Smily
        fields = '__all__'


class SmilyGetSerializer(serializers.ModelSerializer):
    # hotel = HotelSerializer(read_only=True)

    class Meta:

        model = Smily
        fields = '__all__'


class FeedbackGetSerializer(serializers.ModelSerializer):
    # hotel = HotelSerializer(read_only=True)
    smily = SmilyGetSerializer(read_only=True)
    class Meta:
        model = Feedback
        fields = '__all__'
