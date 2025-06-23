from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from decimal import Decimal
import json


class MenuViewTest(TestCase):
    """
    Clase de prueba para las vistas del modelo Menu
    """
    
    def setUp(self):
        """
        Método de configuración que se ejecuta antes de cada prueba.
        Crea algunas instancias de prueba del modelo Menu.
        """
        # Crear instancias de prueba del modelo Menu
        self.menu_item1 = Menu.objects.create(
            Title="Greek Salad",
            Price=Decimal('12.50'),
            Inventory=20
        )
        
        self.menu_item2 = Menu.objects.create(
            Title="Bruschetta",
            Price=Decimal('8.99'),
            Inventory=15
        )
        
        self.menu_item3 = Menu.objects.create(
            Title="Lemon Dessert",
            Price=Decimal('6.75'),
            Inventory=30
        )
        
        # Configurar el cliente API para las pruebas
        self.client = APIClient()
    
    def test_getall(self):
        """
        Prueba para recuperar todos los objetos Menu y verificar
        que los datos serializados coincidan con la respuesta.
        """
        # URL para obtener todos los elementos del menú
        url = reverse('menu-list')  # Nombre generado automáticamente por el router para MenuViewSet
        
        # Realizar petición GET
        response = self.client.get(url)
        
        # Verificar que la respuesta sea exitosa
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Obtener todos los objetos Menu de la base de datos
        menu_items = Menu.objects.all()
        
        # Serializar los objetos
        serializer = MenuSerializer(menu_items, many=True)
        
        # Convertir la respuesta a JSON para comparar
        response_data = response.json()
        
        # Verificar que los datos serializados coincidan con la respuesta
        # Como el ViewSet usa paginación, necesitamos acceder a 'results'
        if 'results' in response_data:
            self.assertEqual(response_data['results'], serializer.data)
        else:
            # Si no hay paginación, comparar directamente
            self.assertEqual(response_data, serializer.data)
        
        # Verificar que se devolvieron exactamente 3 elementos
        items_count = len(response_data['results']) if 'results' in response_data else len(response_data)
        self.assertEqual(items_count, 3)
        
        # Verificar que los títulos de los elementos estén presentes
        if 'results' in response_data:
            titles = [item['Title'] for item in response_data['results']]
        else:
            titles = [item['Title'] for item in response_data]
        
        self.assertIn("Greek Salad", titles)
        self.assertIn("Bruschetta", titles)
        self.assertIn("Lemon Dessert", titles)
