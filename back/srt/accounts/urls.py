from django.contrib import admin
from django.urls import path, include
from .views import KakaoLogin, GoogleLogin


urlpatterns = [
    path('rest-auth/kakao/', KakaoLogin.as_view()),
    path('rest-auth/google/', GoogleLogin.as_view()),
]


