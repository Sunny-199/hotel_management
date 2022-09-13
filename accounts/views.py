from rest_framework.permissions import AllowAny
from .serializers import *
from .models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from . import flat_file
from django.conf import settings
import json
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdmin
from main_app.helper_functions import get_role_id


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


# Token authentication
class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny, ]
    serializer_class = MyTokenObtainPairSerializer


# Assign role to user
class UserRole(ModelViewSet):
    permission_classes = [AllowAny, ]
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def list(self, request, *args, **kwargs):
        data, context = [], {}
        try:
            role_name = request.query_params.get('role_name')
            if role_name:
                role = Role.objects.get(role_name=request.query_params.get('role_name'))
                serializer = RoleSerializer(role)
                data = serializer.data
                data['permissions'] = json.loads(data['permissions'])
                context = custom_response(status.HTTP_200_OK, data,
                                          message="General manager role fetched successfully.")
            else:
                queryset = Role.objects.all()
                serializer = RoleSerializer(queryset, many=True)
                for obj in serializer.data:
                    obj['permissions'] = json.loads(obj['permissions'])
                context = custom_response(status.HTTP_200_OK, serializer.data, "Fetched Successfully.")
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return JsonResponse(context, safe=False, status=context.get("status"))

    def create(self, request, *args, **kwargs):
        data, context = [], {}
        try:
            data = request.data
            permissions = json.dumps(data.get("permissions"))
            data["permissions"] = permissions
            serializer = RoleSerializer(data=request.data)
            if serializer.is_valid():
                self.perform_create(serializer)
                context = custom_response(status.HTTP_201_CREATED, serializer.data,  "Created Successfully.")
            else:
                context = custom_response(status.HTTP_202_ACCEPTED, serializer.errors,  "Unsuccessful.")
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))

        return JsonResponse(context, safe=False, status=context.get("status"))


# User Register Crud
class UserEdit(ModelViewSet):
    permission_classes = [AllowAny, ]
    queryset = User.objects.all()
    # serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        data, context = [], {}
        try:
            hotel_ids = []
            user_id = request.query_params.get("user_id")
            hotel_id = request.query_params.get("hotel_id")
            if user_id:
                users = Hotel.objects.filter(user_id=user_id)
                if users:
                    for user in users:
                        hotel_ids.append(user.id)
                    queryset = User.objects.filter(hotel_id__in=hotel_ids, is_staff=True)
                    serializer = GetUserSerializer(queryset, many=True)
                    for obj in serializer.data:
                        obj['roles']['permissions'] = json.loads(obj['roles']['permissions'])
                    context = custom_response(status.HTTP_200_OK, serializer.data, message="Data fetched Successfully.")
                else:
                    context = custom_response(status.HTTP_404_NOT_FOUND)
            elif hotel_id:
                users = Hotel.objects.filter(id=hotel_id)
                if users:
                    # for user in users:
                    #     hotel_ids.append(user.id)
                    queryset = User.objects.filter(hotel_id=hotel_id, is_staff=True)
                    serializer = GetUserSerializer(queryset, many=True)
                    for obj in serializer.data:
                        obj['roles']['permissions'] = json.loads(obj['roles']['permissions'])
                    context = custom_response(status.HTTP_200_OK, serializer.data, message="Data fetched Successfully.")
                else:
                    context = custom_response(status.HTTP_404_NOT_FOUND)
            else:
                queryset = User.objects.all()
                serializer = UserSerializerGet(queryset, many=True)
                for obj in serializer.data:
                    obj['roles']['permissions'] = json.loads(obj['roles']['permissions'])
                context = custom_response(status.HTTP_200_OK, serializer.data, "Fetched Successfully.")
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return JsonResponse(context, safe=False, status=context.get("status"))

    def create(self, request, *args, **kwargs):
        data, context = [], {}
        try:
            data = request.data
            serializer = UserSerializer(data=data)
            role_id = get_role_id(data)
            data["roles"] = role_id
            if serializer.is_valid():
                self.perform_create(serializer)
                user_obj = User.objects.get(id=serializer.data["id"])
                serializer = UserSerializerGet(user_obj)
                serializer.data['roles']['permissions'] = json.loads(serializer.data['roles']['permissions'])
                context = custom_response(status.HTTP_201_CREATED, serializer.data, "Created Successfully.")
            else:
                context = custom_response(status.HTTP_409_CONFLICT, serializer.errors, "Unsuccessful.")
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return JsonResponse(context, status=context['status'], safe=False)

    def partial_update(self, request, pk):
        data = []
        try:
            try:
                queryset = User.objects.all()
                user = get_object_or_404(queryset, pk=pk)
                serializer = UserRoomSerializer(user, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    user_obj = User.objects.get(id=serializer.data["id"])
                    serializer = GetUserSerializer(user_obj)
                    serializer.data['roles']["permissions"] = json.loads(serializer.data['roles']["permissions"])
                    context = custom_response(status.HTTP_200_OK, serializer.data, "Updated Successfully.")
                else:
                    context = custom_response(status.HTTP_202_ACCEPTED, serializer.errors, "Unsuccessful.")
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
                get_user = User.objects.get(id=pk)
                serializer = UserSerializerGet(get_user)
                serializer.data['roles']["permissions"] = json.loads(serializer.data['roles']["permissions"])
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
                user = self.get_object()
                user.delete()
                context = custom_response(status.HTTP_200_OK, message="Deleted Successfully")
            except Exception as error:
                context = custom_response(status.HTTP_404_NOT_FOUND)
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return JsonResponse(context, status=context.get('status'), safe=False)


class FlatToken(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        try:
            PRIVATE_KEY = settings.PRIVATE_KEY
            EMBED_ID = settings.EMBED_ID
            flat_token = flat_file.token(EMBED_ID, PRIVATE_KEY)
            context = custom_response(status.HTTP_200_OK, flat_token.get('token'), message="Token fetched Successfully.")
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return JsonResponse(context, status=context.get('status'), safe=False)


# class GetStaff(APIView):
#
#     def get(self, request):
#         try:
#             hotel_ids = []
#             user_id = request.query_params.get("user_id")
#             users = Hotel.objects.filter(user_id=user_id)
#             if users:
#                 for user in users:
#                     hotel_ids.append(user.id)
#                 queryset = User.objects.filter(hotel_id__in=hotel_ids, is_staff=True)
#                 serializer = GetUserSerializer(queryset, many=True)
#                 for obj in serializer.data:
#                     obj['roles']['permissions'] = json.loads(obj['roles']['permissions'])
#                 context = custom_response(status.HTTP_200_OK, serializer.data, message="Data fetched Successfully.")
#             else:
#                 context = custom_response(status.HTTP_404_NOT_FOUND)
#         except Exception as error:
#             context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
#         return JsonResponse(context, status=context.get('status'), safe=False)
