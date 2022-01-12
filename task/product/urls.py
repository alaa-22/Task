from django.urls import path
from .views import all_products, create_product,\
    product_filter, get_user_product

urlpatterns = [
    path('', all_products, name="all product"),
    path('filter/username/<str:name>/', product_filter, name="serch_product"),
    path('create/', create_product, name="create_product"),
    path('myproduct/', get_user_product, name="user_products"),

]
