from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from rest_framework.decorators import api_view, permission_classes
from .models import ProductModel
from .filters import ProductFilter


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_products(request, ):
    product = ProductModel.objects.order_by('price')
    filterset = ProductFilter(request.GET, queryset=product)
    product = filterset.qs
    serializer = ProductSerializer(product, many=True)

    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_product(request):
    try:
        ProductModel.objects.create(
            seller=request.user,
            name=request.data['name'],
            price=request.data['price']
        )
        return Response(status=status.HTTP_201_CREATED)

    except:
        return Response({'datails': 'please correct data'},
                        status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_product(request):
    product = \
        ProductModel.objects.filter(seller=request.user).order_by('price')
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)
