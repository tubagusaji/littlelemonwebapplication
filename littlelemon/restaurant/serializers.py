from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Booking, Menu, MenuItem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ['name', 'no_of_guests', 'booking_date']

class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = ['title', 'price', 'inventory']

class MenuItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItem
        fields = ['title', 'price', 'inventory']