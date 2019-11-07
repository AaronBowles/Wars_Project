from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('wars', views.WarList.as_view(), name='war_list'),
    path('wars/<int:pk', views.WarDetail.as_view(), name='war_detail'),
]