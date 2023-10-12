from django.urls import path
from .views import *

urlpatterns = [
    path('Register/', UserRegistration.as_view()),
    path('login/', Login.as_view()),
]