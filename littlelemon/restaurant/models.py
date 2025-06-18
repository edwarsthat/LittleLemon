from django.db import models

# Create your models here.

class Booking(models.Model):
    """
    Modelo para manejar las reservas del restaurante Little Lemon
    """
    # ID se crea automáticamente por Django como AutoField primary key
    Name = models.CharField(max_length=255, help_text="Nombre del cliente")
    No_of_guests = models.IntegerField(help_text="Número de invitados")
    BookingDate = models.DateTimeField(help_text="Fecha y hora de la reserva")
    
    class Meta:
        db_table = 'restaurant_booking'
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ['BookingDate']
    
    def __str__(self):
        return f"{self.Name} - {self.No_of_guests} invitados - {self.BookingDate.strftime('%d/%m/%Y %H:%M')}"


class Menu(models.Model):
    """
    Modelo para manejar los elementos del menú del restaurante Little Lemon
    """
    # ID se crea automáticamente por Django como AutoField primary key
    Title = models.CharField(max_length=255, help_text="Título del plato")
    Price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Precio del plato")
    Inventory = models.IntegerField(help_text="Inventario disponible")
    
    class Meta:
        db_table = 'restaurant_menu'
        verbose_name = 'Elemento del Menú'
        verbose_name_plural = 'Elementos del Menú'
        ordering = ['Title']
    
    def __str__(self):
        return f"{self.Title} - ${self.Price} (Stock: {self.Inventory})"
