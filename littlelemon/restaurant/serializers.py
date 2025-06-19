from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Booking, Menu


class UserSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo User de Django
    """
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class BookingSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Booking
    """
    class Meta:
        model = Booking
        fields = ['id', 'Name', 'No_of_guests', 'BookingDate']


class MenuSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Menu
    """
    class Meta:
        model = Menu
        fields = ['id', 'Title', 'Price', 'Inventory']
