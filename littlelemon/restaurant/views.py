from rest_framework import generics, viewsets
from .models import Menu, Booking, MenuItem
from .serializers import MenuSerializer, BookingSerializer, MenuItemSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes

@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})

def index(request):
    return render(request,'index.html', {})

# Create your views here. 
class MenuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated] 
    # def list(self, request):
    #     queryset = Booking.objects.all()
    #     serializer = BookingSerializer(queryset, many=True)
    #     return Response(serializer.data)

class MenuItemsView(generics.ListCreateAPIView):
      permission_classes = [IsAuthenticated]
      queryset = MenuItem.objects.all()
      serializer_class = MenuItemSerializer