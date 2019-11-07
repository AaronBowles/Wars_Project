from django.urls import path
from . import views
#from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.war_list, name='war_list'),
    path('wars/<int:pk>', views.war_detail, name='war_detail'),
    path('wars/new', views.war_create, name='war_create'),
    path('wars/<int:pk>/edit', views.war_edit, name='war_edit'),
    path('wars/<int:pk>/delete', views.war_delete, name='war_delete'),

    path('battles', views.battle_list, name='battle_list')battlepath('battles/<int:pk>', views.war_detail, name='battle_detail'),
    path('battles/new', views.war_create, name='battle_create'),
    path('battles/<int:pk>/edit', views.war_edit, name='battle_edit'),
    path('battles/<int:pk>/delete', views.war_delete, name='battle_delete'),

]

# urlpatterns = [
#     path('wars', views.WarList.as_view(), name='war_list'),
#     path('wars/<int:pk', views.WarDetail.as_view(), name='war_detail'),
# ]