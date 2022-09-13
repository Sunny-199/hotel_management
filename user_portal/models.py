from django.db import models
from main_app.models import Hotel
from django.conf import settings
from django.contrib.postgres.fields import ArrayField


class Smily(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, blank=True)
    smily = models.CharField(max_length=100, null=True, blank=True)
    mood = ArrayField(models.CharField(max_length=10, blank=True, null=True), size=8,)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


# class SmilyOption(models.Model):
#     smily = models.ForeignKey(Smily, on_delete=models.CASCADE, null=True, blank=True)
#     mood = models.CharField(max_length=100, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
#     updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


class Feedback(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, blank=True)
    # keyword = models.CharField(max_length=100, null=True, blank=True)
    smily = models.ForeignKey(Smily, on_delete=models.CASCADE, null=True, blank=True)
    mood = models.CharField(max_length=100, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    # is_selected = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
