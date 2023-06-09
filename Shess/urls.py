"""Shess URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from chess.views import *
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'masters',ChessViewSet,basename='masters')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('',include('chess.urls')),
    path('api/v1/Chess/', ChessAPIList.as_view()),
    path('api/v1/Chess/<int:pk>/', ChessAPIUpdate.as_view()),
    path('api/v1/Chessdelete/<int:pk>/', ChessAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),  # new
    re_path(r'^auth/', include('djoser.urls.authtoken')),  # new
    # path('api/v1/accounts/', include('djoser.urls')), чтобы не ломалась форма авторизации
    # path('api/v1/accounts/token/', include('djoser.urls.authtoken')),
    # path('api/v1/',include(router.urls))  # http://127.0.0.1:8000/api/v1/masters
]


