# Little Lemon Restaurant API

Este es el proyecto backend para el restaurante Little Lemon, desarrollado con Django y Django REST Framework.

## 📋 Descripción

Little Lemon es una API RESTful que proporciona funcionalidades completas para la gestión de un restaurante, incluyendo manejo de menús, reservas, pedidos y autenticación de usuarios.

## 🚀 Características

- API RESTful completa
- Autenticación y autorización de usuarios
- Gestión de menús y categorías
- Sistema de reservas
- Gestión de pedidos
- Panel de administración de Django
- Documentación de API integrada

## 🛠️ Tecnologías Utilizadas

- **Python 3.10+**
- **Django 5.2.3**
- **Django REST Framework**
- **SQLite** (Base de datos por defecto)

## 📦 Instalación

### Prerrequisitos

- Python 3.10 o superior
- pip (Gestor de paquetes de Python)
- Git

### Pasos de instalación

1. **Clonar el repositorio**
   ```bash
   git clone git@github.com:edwardo1239/LittleLemon.git
   cd LittleLemon
   ```

2. **Crear y activar el entorno virtual**
   ```bash
   # Windows
   python -m venv env
   env\Scripts\activate

   # macOS/Linux
   python -m venv env
   source env/bin/activate
   ```

3. **Instalar las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar la base de datos**
   ```bash
   cd littlelemon
   python manage.py migrate
   ```

5. **Crear un superusuario (opcional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Ejecutar el servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

El servidor estará disponible en `http://127.0.0.1:8000/`

## 🔧 Configuración

### Variables de Entorno

Crea un archivo `.env` en el directorio raíz del proyecto con las siguientes variables:

```env
SECRET_KEY=tu_clave_secreta_aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Base de Datos

Por defecto, el proyecto utiliza SQLite. Para cambiar a PostgreSQL o MySQL, modifica la configuración en `littlelemon/settings.py`.

## 📚 Uso de la API

### Endpoints Principales

- **Admin Panel**: `http://127.0.0.1:8000/admin/`
- **API Root**: `http://127.0.0.1:8000/api/`

### Autenticación

La API utiliza autenticación basada en tokens. Para obtener un token:

```bash
POST /api/auth/token/
{
    "username": "tu_usuario",
    "password": "tu_contraseña"
}
```

### Ejemplos de Uso

```bash
# Obtener lista de menús
GET /api/menu/

# Crear una nueva reserva
POST /api/bookings/
{
    "name": "Juan Pérez",
    "date": "2025-06-20",
    "time": "19:00",
    "guests": 4
}
```

## 🧪 Testing

Para ejecutar las pruebas:

```bash
cd littlelemon
python manage.py test
```

## 📁 Estructura del Proyecto

```
littlelemon/
├── manage.py
├── db.sqlite3
├── littlelemon/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── apps/
    ├── menu/
    ├── bookings/
    └── users/
```

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu característica (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -am 'Añadir nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👥 Autor

- **Eduardo** - *Desarrollo inicial* - [@edwardo1239](https://github.com/edwardo1239)

## 🆘 Soporte

Si tienes alguna pregunta o problema, por favor:

1. Revisa la documentación
2. Busca en los issues existentes
3. Crea un nuevo issue si es necesario

## 📈 Roadmap

- [ ] Implementar sistema de pagos
- [ ] Añadir notificaciones en tiempo real
- [ ] Integrar con servicios de delivery
- [ ] Mejorar la documentación de la API
- [ ] Añadir más tests unitarios

---

⭐ Si este proyecto te ha sido útil, ¡no olvides darle una estrella!
