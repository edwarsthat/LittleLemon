from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from rest_framework import status, viewsets, mixins, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Booking, Menu
from .serializers import UserSerializer, BookingSerializer, MenuSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


# ===========================================
# 1. FUNCTION-BASED VIEWS
# ===========================================

@api_view(['GET', 'POST'])
def user_list_function(request):
    """
    Function-based view para listar usuarios o crear uno nuevo
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True, context={'request': request})
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_function(request, pk):
    """
    Function-based view para obtener, actualizar o eliminar un usuario específico
    """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ===========================================
# 2. CLASS-BASED VIEWS (APIView)
# ===========================================

class BookingListAPIView(APIView):
    """
    Class-based view para listar reservas o crear una nueva
    """
    def get(self, request):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookingDetailAPIView(APIView):
    """
    Class-based view para obtener, actualizar o eliminar una reserva específica
    """
    def get_object(self, pk):
        try:
            return Booking.objects.get(pk=pk)
        except Booking.DoesNotExist:
            return None
    
    def get(self, request, pk):
        booking = self.get_object(pk)
        if not booking:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookingSerializer(booking)
        return Response(serializer.data)
    
    def put(self, request, pk):
        booking = self.get_object(pk)
        if not booking:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookingSerializer(booking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        booking = self.get_object(pk)
        if not booking:
            return Response(status=status.HTTP_404_NOT_FOUND)
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ===========================================
# 3. MIXINS
# ===========================================

class MenuListMixin(mixins.ListModelMixin, 
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
    """
    Vista usando mixins para listar y crear elementos del menú
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MenuDetailMixin(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    """
    Vista usando mixins para obtener, actualizar y eliminar elementos del menú
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# ===========================================
# 4. GENERIC VIEW CLASSES
# ===========================================

class UserListGeneric(generics.ListCreateAPIView):
    """
    Generic view para listar y crear usuarios
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    """
    Generic view para obtener, actualizar y eliminar usuarios
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookingListGeneric(generics.ListCreateAPIView):
    """
    Generic view para listar y crear reservas
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class BookingDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    """
    Generic view para obtener, actualizar y eliminar reservas
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


# ===========================================
# 5. VIEWSETS
# ===========================================

class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet que proporciona automáticamente acciones CRUD para usuarios
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookingViewSet(viewsets.ModelViewSet):
    """
    ViewSet que proporciona automáticamente acciones CRUD para reservas
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class MenuViewSet(viewsets.ModelViewSet):
    """
    ViewSet que proporciona automáticamente acciones CRUD para menú
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


# ===========================================
# VIEWSET PERSONALIZADO CON ACCIONES LIMITADAS
# ===========================================

class MenuReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet de solo lectura para el menú (GET solamente)
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer