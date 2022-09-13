from accounts.views import *
from .serializers import *
from .models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from accounts.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from django.http import JsonResponse


def custom_response(status, data=[], message=""):
    if status == 404:
        if not message:
            message = "Data not found."
        context = {
            "status": status,
            "message": message,
            "data": data
        }
    elif status == 400 or status == 202:
        error_list = list()
        if isinstance(data, str):
            message = data
            context = {
                "status": status,
                "message": message,
                "data": []
            }
        else:
            for i, j in data.items():
                j = "".join(j)
                message = f"{i}: {j}"
                error_list.append(message)

            context = {
                "status": status,
                "message": ", ".join(error_list),
                "data": []
            }
    elif status == 409:
        context = {
            "status": status,
            "message": "Already exists",
            "data": []
        }
    else:
        context = {
            "status": status,
            "message": message,
            "data": data
        }
    return context


class CouponDetails(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

    def list(self, request, *args, **kwargs):
        data, context = [], {}
        try:
            queryset = Coupon.objects.all()
            if queryset:
                serializer = CouponSerializer(queryset, many=True)
                context = custom_response(status.HTTP_200_OK, serializer.data, message="Fetched Successfully")
            else:
                context = custom_response(status.HTTP_404_NOT_FOUND)
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return JsonResponse(context, safe=False, status=context.get("status"))

    def create(self, request, *args, **kwargs):
        data, context = [], {}
        try:
            serializer = CouponSerializer(data=request.data)
            if serializer.is_valid():
                check = Coupon.objects.filter(hotel=request.data.get("hotel"), name=request.data.get("name"))
                if check.count() == 0:
                    self.perform_create(serializer)
                    coupon_obj = Coupon.objects.get(id=serializer.data["id"])
                    serializer = CouponSerializer(coupon_obj)
                    context = custom_response(status.HTTP_201_CREATED, serializer.data, message="Created Successfully.")
                else:
                    context = custom_response(status.HTTP_409_CONFLICT)
            else:
                context = custom_response(status.HTTP_202_ACCEPTED, serializer.errors, message="Unsuccessful.")
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return JsonResponse(context, safe=False)

    def partial_update(self, request, pk):
        data = []
        try:
            try:
                queryset = Coupon.objects.all()
                coupon = get_object_or_404(queryset, pk=pk)
                serializer = CouponSerializer(coupon, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    coupon_obj = Coupon.objects.get(id=serializer.data["id"])
                    serializer = CouponSerializer(coupon_obj)
                    context = custom_response(status.HTTP_200_OK, serializer.data, message="Updated Successfully.")
                    return Response(context, status=context.get("status"))
                else:
                    context = custom_response(status.HTTP_202_ACCEPTED, serializer.errors, message="Unsuccessful.")
                    return Response(context, status=context.get("status"))
            except Exception as error:
                context = custom_response(status.HTTP_404_NOT_FOUND)
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return Response(context, status=context.get("status"))

    def retrieve(self, request, pk=None):
        data = []
        context = {}
        try:
            try:
                get_coupon = Coupon.objects.get(id=pk)
                serializer = CouponSerializer(get_coupon)
                context = custom_response(status.HTTP_200_OK, serializer.data, "Fetched Successfully.")
            except Exception as error:
                context = custom_response(status.HTTP_404_NOT_FOUND)
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return JsonResponse(context, status=context.get("status"), safe=False)

    def destroy(self, request, *args, **kwargs):
        data, context = [], {}
        try:
            try:
                coupon = self.get_object()
                coupon.delete()
                context = custom_response(status.HTTP_200_OK, message="Deleted Successfully.")
            except Exception as error:
                context = custom_response(status.HTTP_404_NOT_FOUND)
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))

        return JsonResponse(context, status=context.get('status'), safe=False)


class PromotionDetails(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Promotions.objects.all()
    serializer_class = PromotionSerializer

    def list(self, request, *args, **kwargs):
        data, context = [], {}
        try:
            queryset = Promotions.objects.all()
            if queryset:
                serializer = PromotionSerializer(queryset, many=True)
                context = custom_response(status.HTTP_200_OK, serializer.data, message="Fetched Successfully")
            else:
                context = custom_response(status.HTTP_404_NOT_FOUND)
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return JsonResponse(context, safe=False, status=context.get("status"))

    def create(self, request, *args, **kwargs):
        data, context = [], {}
        try:
            serializer = PromotionSerializer(data=request.data)
            if serializer.is_valid():
                check = Promotions.objects.filter(hotel=request.data.get("hotel"), name=request.data.get("name"))
                if check.count() == 0:
                    self.perform_create(serializer)
                    promotion_obj = Promotions.objects.get(id=serializer.data["id"])
                    serializer = PromotionSerializer(promotion_obj)
                    context = custom_response(status.HTTP_201_CREATED, serializer.data, message="Created Successfully.")
                else:
                    context = custom_response(status.HTTP_409_CONFLICT)
            else:
                context = custom_response(status.HTTP_202_ACCEPTED, serializer.errors, message="Unsuccessful.")
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return JsonResponse(context, safe=False)

    def partial_update(self, request, pk):
        data = []
        try:
            try:
                queryset = Promotions.objects.all()
                promotion = get_object_or_404(queryset, pk=pk)
                serializer = PromotionSerializer(promotion, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    promotion_obj = Promotions.objects.get(id=serializer.data["id"])
                    serializer = PromotionSerializer(promotion_obj)
                    context = custom_response(status.HTTP_200_OK, serializer.data, message="Updated Successfully.")
                    return Response(context, status=context.get("status"))
                else:
                    context = custom_response(status.HTTP_202_ACCEPTED, serializer.errors, message="Unsuccessful.")
                    return Response(context, status=context.get("status"))
            except Exception as error:
                context = custom_response(status.HTTP_404_NOT_FOUND)
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return Response(context, status=context.get("status"))

    def retrieve(self, request, pk=None):
        data = []
        context = {}
        try:
            try:
                get_promotion = Promotions.objects.get(id=pk)
                serializer = PromotionSerializer(get_promotion)
                context = custom_response(status.HTTP_200_OK, serializer.data, "Fetched Successfully.")
            except Exception as error:
                context = custom_response(status.HTTP_404_NOT_FOUND)
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return JsonResponse(context, status=context.get("status"), safe=False)

    def destroy(self, request, *args, **kwargs):
        data, context = [], {}
        try:
            try:
                promotion = self.get_object()
                promotion.delete()
                context = custom_response(status.HTTP_200_OK, message="Deleted Successfully.")
            except Exception as error:
                context = custom_response(status.HTTP_404_NOT_FOUND)
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))

        return JsonResponse(context, status=context.get('status'), safe=False)


class SliderDetails(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Slider.objects.all()
    serializer_class = PromotionSerializer

    def list(self, request, *args, **kwargs):
        data, context = [], {}
        try:
            queryset = Slider.objects.all()
            if queryset:
                serializer = SliderSerializerGet(queryset, many=True)
                context = custom_response(status.HTTP_200_OK, serializer.data, message="Fetched Successfully")
            else:
                context = custom_response(status.HTTP_404_NOT_FOUND)
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return JsonResponse(context, safe=False, status=context.get("status"))

    def create(self, request, *args, **kwargs):
        data, context = [], {}
        try:
            serializer = SliderSerializerEdit(data=request.data)
            if serializer.is_valid():
                check = Slider.objects.filter(hotel=request.data.get("hotel"), name=request.data.get("name"))
                if check.count() == 0:
                    self.perform_create(serializer)
                    slider_obj = Slider.objects.get(id=serializer.data["id"])
                    serializer = SliderSerializerGet(slider_obj)
                    context = custom_response(status.HTTP_201_CREATED, serializer.data, message="Created Successfully.")
                else:
                    context = custom_response(status.HTTP_409_CONFLICT)
            else:
                context = custom_response(status.HTTP_202_ACCEPTED, serializer.errors, message="Unsuccessful.")
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return JsonResponse(context, safe=False)

    def partial_update(self, request, pk):
        data = []
        try:
            try:
                queryset = Slider.objects.all()
                slider = get_object_or_404(queryset, pk=pk)
                serializer = SliderSerializerGet(slider, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    slider_obj = Slider.objects.get(id=serializer.data["id"])
                    serializer = SliderSerializerGet(slider_obj)
                    context = custom_response(status.HTTP_200_OK, serializer.data, message="Updated Successfully.")
                    return Response(context, status=context.get("status"))
                else:
                    context = custom_response(status.HTTP_202_ACCEPTED, serializer.errors, message="Unsuccessful.")
                    return Response(context, status=context.get("status"))
            except Exception as error:
                context = custom_response(status.HTTP_404_NOT_FOUND)
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return Response(context, status=context.get("status"))

    def retrieve(self, request, pk=None):
        data = []
        context = {}
        try:
            try:
                get_slider = Slider.objects.get(id=pk)
                serializer = SliderSerializerGet(get_slider)
                context = custom_response(status.HTTP_200_OK, serializer.data, "Fetched Successfully.")
            except Exception as error:
                context = custom_response(status.HTTP_404_NOT_FOUND)
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return JsonResponse(context, status=context.get("status"), safe=False)

    def destroy(self, request, *args, **kwargs):
        data, context = [], {}
        try:
            try:
                slider = self.get_object()
                slider.delete()
                context = custom_response(status.HTTP_200_OK, message="Deleted Successfully.")
            except Exception as error:
                context = custom_response(status.HTTP_404_NOT_FOUND)
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return JsonResponse(context, status=context.get('status'), safe=False)
