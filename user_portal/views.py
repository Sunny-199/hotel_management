from accounts.views import *
from .serializers import FeedbackGetSerializer, FeedbackEditSerializer, SmilyGetSerializer, \
    SmilyEditSerializer
from .models import Feedback, Smily
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


class SmilyDetails(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Smily.objects.all()
    serializer_class = SmilyGetSerializer

    def list(self, request, *args, **kwargs):
        data, context = [], {}
        try:
            queryset = Smily.objects.all()
            if queryset:
                serializer = SmilyGetSerializer(queryset, many=True)
                context = custom_response(status.HTTP_200_OK, serializer.data, message="Fetched Successfully")
            else:
                context = custom_response(status.HTTP_404_NOT_FOUND)
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return JsonResponse(context, safe=False, status=context.get("status"))

    def create(self, request, *args, **kwargs):
        data, context = [], {}
        try:
            data = request.data
            mood = data.get("mood")
            smily = data.get('smily')
            serializer = SmilyEditSerializer(data=data)
            if serializer.is_valid():
                check = Smily.objects.filter(hotel=data.get('hotel'), mood__contains=mood, smily=smily)
                if check.count() == 0:
                    self.perform_create(serializer)
                    smily_obj = Smily.objects.get(id=serializer.data["id"])
                    serializer = SmilyEditSerializer(smily_obj)
                    context = custom_response(status.HTTP_201_CREATED, serializer.data, message="Created Successfully.")
                else:
                    context = custom_response(status.HTTP_409_CONFLICT)
            else:
                context = custom_response(status.HTTP_202_ACCEPTED, serializer.errors, message="Unsuccessful.")
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return JsonResponse(context, safe=False, status=status.HTTP_409_CONFLICT)

    def partial_update(self, request, pk):
        data = []
        try:
            try:
                queryset = Smily.objects.all()
                smily = get_object_or_404(queryset, pk=pk)
                serializer = SmilyEditSerializer(smily, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    smily_obj = Smily.objects.get(id=serializer.data["id"])
                    serializer = SmilyEditSerializer(smily_obj)
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
                get_Smily = Smily.objects.get(id=pk)
                serializer = SmilyEditSerializer(get_Smily)
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
                Smily = self.get_object()
                Smily.delete()
                context = custom_response(status.HTTP_200_OK, message="Deleted Successfully.")
            except Exception as error:
                context = custom_response(status.HTTP_404_NOT_FOUND)
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))

        return JsonResponse(context, status=context.get('status'), safe=False)


class FeedbackDetails(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Feedback.objects.all()
    serializer_class = FeedbackGetSerializer

    def list(self, request, *args, **kwargs):
        data, context = [], {}
        try:
            queryset = Feedback.objects.all()
            if queryset:
                serializer = FeedbackGetSerializer(queryset, many=True)
                context = custom_response(status.HTTP_200_OK, serializer.data, message="Fetched Successfully")
            else:
                context = custom_response(status.HTTP_404_NOT_FOUND)
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return JsonResponse(context, safe=False, status=context.get("status"))

    def create(self, request, *args, **kwargs):
        data, context = [], {}
        try:

            data = request.data
            serializer = FeedbackEditSerializer(data=data)
            if serializer.is_valid():
                self.perform_create(serializer)
                feedback_obj = Feedback.objects.get(id=serializer.data["id"])
                serializer = FeedbackGetSerializer(feedback_obj)
                context = custom_response(status.HTTP_201_CREATED, serializer.data, message="Created Successfully.")
            else:
                context = custom_response(status.HTTP_202_ACCEPTED, serializer.errors, message="Unsuccessful.")
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return JsonResponse(context, safe=False, status=status.HTTP_409_CONFLICT)

    def partial_update(self, request, pk):
        data = []
        try:
            try:
                queryset = Feedback.objects.all()
                feedback = get_object_or_404(queryset, pk=pk)
                serializer = FeedbackEditSerializer(feedback, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    feedback_obj = Feedback.objects.get(id=serializer.data["id"])
                    serializer = FeedbackGetSerializer(feedback_obj)
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
                get_feedback = Feedback.objects.get(id=pk)
                serializer = FeedbackGetSerializer(get_feedback)
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
                feedback = self.get_object()
                feedback.delete()
                context = custom_response(status.HTTP_200_OK, message="Deleted Successfully.")
            except Exception as error:
                context = custom_response(status.HTTP_404_NOT_FOUND)
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))

        return JsonResponse(context, status=context.get('status'), safe=False)

