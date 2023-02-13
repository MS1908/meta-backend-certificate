from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import MenuItem
from .serializers import MenuItemSerializer

# Create your views here.


class ListMenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
    
class DetailMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        if request.user.groups.filter(name='Manager').exists():
            pass
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
    def patch(self, request, *args, **kwargs):
        if request.user.groups.filter(name='Manager').exists():
            pass
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
    def delete(self, request, *args, **kwargs):
        if request.user.groups.filter(name='Manager').exists():
            pass
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
