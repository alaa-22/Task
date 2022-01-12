from django.urls import path
from .views import MyObtainTokenPairView, register

urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name="login"),
    path('register/', register, name="login"),
]
