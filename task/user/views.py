from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
# Create your views here.
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import MyTokenObtainPairSerializer


@api_view(['POST'])
def register(request):
    try:
        password = make_password(request.data['password'])
        User.objects.create(
            last_name=request.data['last_name'],
            first_name=request.data['first_name'],
            username=request.data['username'],
            email=request.data['email'],
            password=password
        )
        return Response(status=status.HTTP_201_CREATED)
    except:
        print(request.data)
        return Response({'details': 'error'},
                        status=status.HTTP_400_BAD_REQUEST)


class MyObtainTokenPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
