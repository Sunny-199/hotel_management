import json
from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# role serializers
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


# class GetGMRoleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Role
#         exclude = ['hotel', ]


class UserSerializerGet(serializers.ModelSerializer):
    roles = RoleSerializer(read_only=True)

    class Meta:
        model = User
        exclude = ['password', 'groups', "user_permissions"]


class UserSerializer(serializers.ModelSerializer):
    """user serializer"""

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    USERNAME_FIELD = 'email'

    def validate(self, attrs):
        password = attrs.get('password')
        user_obj = User.objects.filter(email=attrs.get('email'))
        if user_obj:
            credentials = {
                'email': user_obj[0].email,
                'password': password
            }
            user = User.objects.get(email=user_obj[0].email)
            user_data = GetUserSerializer(user).data
            user_data["roles"]["permissions"] = json.loads(user_data["roles"]["permissions"])
            # print(user.check_password(password))
            if user.check_password(password):
                refresh = self.get_token(user)
                data = {
                    'success': True,
                    'status': 200,
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'email': user.email,
                    'message': 'Login successfully',
                    'user': user_data
                }
                return data
            return {"message": 'please enter valid email and password', 'status': 400}
        else:
            return {"message": 'please enter valid email and password', 'status': 400}

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token


class GetUserSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(read_only=True)

    class Meta:
        model = User
        exclude = ['password', 'groups', "user_permissions"]


class UserRoomSerializer(serializers.ModelSerializer):
    """user serializer"""

    class Meta:
        model = User
        exclude = ['password', 'groups', "user_permissions"]
