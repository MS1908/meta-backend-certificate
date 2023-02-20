from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('menu-items', views.ListMenuItemsView.as_view()),
    path('menu-items/<str:menuitem>', views.DetailMenuItemView.as_view())
]
