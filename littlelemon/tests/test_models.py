from django.test import TestCase
from restaurant.models import Menu
from decimal import Decimal


class MenuTest(TestCase):
    """
    Clase de prueba para el modelo Menu
    """
    
    def test_menu_creation(self):
        """
        Prueba la creación de una instancia del modelo Menu
        y verifica su representación en cadena
        """
        # Crear una nueva instancia del modelo Menu
        menu_item = Menu.objects.create(
            Title="Pasta Carbonara",
            Price=Decimal('15.99'),
            Inventory=25
        )
        
        # Verificar que la representación en cadena sea la esperada
        expected_string = "Pasta Carbonara - $15.99 (Stock: 25)"
        self.assertEqual(str(menu_item), expected_string)
    
    def test_menu_fields(self):
        """
        Prueba adicional para verificar que los campos se guarden correctamente
        """
        # Crear una nueva instancia del modelo Menu
        menu_item = Menu.objects.create(
            Title="Caesar Salad",
            Price=Decimal('12.50'),
            Inventory=15
        )
        
        # Verificar que los campos se hayan guardado correctamente
        self.assertEqual(menu_item.Title, "Caesar Salad")
        self.assertEqual(menu_item.Price, Decimal('12.50'))
        self.assertEqual(menu_item.Inventory, 15)
