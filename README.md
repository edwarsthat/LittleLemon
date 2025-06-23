# Little Lemon Restaurant API

Este es el proyecto backend para el restaurante Little Lemon, desarrollado con Django y Django REST Framework.

## 📋 Descripción

Little Lemon es una API RESTful que proporciona funcionalidades completas para la gestión de un restaurante, incluyendo manejo de menús, reservas, pedidos y autenticación de usuarios.

## 🚀 Características

- **API RESTful completa** con operaciones CRUD
- **Autenticación por tokens** con Djoser
- **Gestión de menús** (solo administradores)
- **Sistema de reservas** (usuarios autenticados)
- **Múltiples tipos de vistas** (ViewSets, Function-based, Class-based, Mixins, Generic)
- **Seguridad robusta** con permisos diferenciados
- **Panel de administración** de Django
- **Tests automatizados** para modelos y vistas
- **Documentación completa** de la API

## 🛠️ Tecnologías Utilizadas

- **Python 3.13+**
- **Django 5.2.3**
- **Django REST Framework 3.15.2**
- **Djoser** (Autenticación con tokens)
- **SQLite** (Base de datos por defecto)
- **Pillow** (Para manejo de imágenes)
- **django-cors-headers** (Para CORS)
- **python-decouple** (Para variables de entorno)

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

### 🔐 Autenticación

La API utiliza **autenticación por tokens** con Djoser. Soporta múltiples métodos:

#### Obtener Token de Autenticación
```bash
POST /auth/token/login/
Content-Type: application/json

{
    "username": "tu_usuario",
    "password": "tu_contraseña"
}
```

**Respuesta exitosa:**
```json
{
    "auth_token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

#### Usar el Token en las Peticiones
Incluye el token en el header `Authorization`:
```bash
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

#### Cerrar Sesión
```bash
POST /auth/token/logout/
Authorization: Token tu_token_aqui
```

### 🌐 Endpoints Principales

#### Panel de Administración
- **Admin Panel**: `http://127.0.0.1:8000/admin/`
- **API Browser**: `http://127.0.0.1:8000/api-auth/`

#### Autenticación (Djoser)
| Método | Endpoint | Descripción | Autenticación |
|--------|----------|-------------|---------------|
| `POST` | `/auth/users/` | Crear nuevo usuario | No requerida |
| `GET` | `/auth/users/me/` | Obtener perfil del usuario actual | Token |
| `POST` | `/auth/users/set_password/` | Cambiar contraseña | Token |
| `POST` | `/auth/token/login/` | Obtener token de autenticación | No requerida |
| `POST` | `/auth/token/logout/` | Cerrar sesión (eliminar token) | Token |

#### API del Restaurante (ViewSets - Recomendado)
| Método | Endpoint | Descripción | Autenticación |
|--------|----------|-------------|---------------|
| `GET` | `/api/menu/` | Listar todos los elementos del menú | No requerida |
| `POST` | `/api/menu/` | Crear nuevo elemento del menú | Admin |
| `GET` | `/api/menu/{id}/` | Obtener elemento específico del menú | No requerida |
| `PUT` | `/api/menu/{id}/` | Actualizar elemento del menú | Admin |
| `DELETE` | `/api/menu/{id}/` | Eliminar elemento del menú | Admin |
| `GET` | `/api/bookings/` | Listar reservas | Token |
| `POST` | `/api/bookings/` | Crear nueva reserva | Token |
| `GET` | `/api/bookings/{id}/` | Obtener reserva específica | Token |
| `PUT` | `/api/bookings/{id}/` | Actualizar reserva | Token |
| `DELETE` | `/api/bookings/{id}/` | Eliminar reserva | Token |
| `GET` | `/api/users/` | Listar usuarios | Token |
| `POST` | `/api/users/` | Crear usuario | Admin |
| `GET` | `/api/users/{id}/` | Obtener usuario específico | Token |
| `PUT` | `/api/users/{id}/` | Actualizar usuario | Admin |
| `DELETE` | `/api/users/{id}/` | Eliminar usuario | Admin |

#### Endpoints Alternativos (Diferentes implementaciones)
| Tipo | Endpoints |
|------|-----------|
| **Function-based** | `/api/function/users/`, `/api/function/users/{id}/` |
| **Class-based** | `/api/class/bookings/`, `/api/class/bookings/{id}/` |
| **Mixins** | `/api/mixin/menu/`, `/api/mixin/menu/{id}/` |
| **Generic Views** | `/api/generic/users/`, `/api/generic/bookings/` |

### 🔧 Ejemplos de Uso

#### 1. Registrar un nuevo usuario
```bash
curl -X POST http://127.0.0.1:8000/auth/users/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "juanperez",
    "email": "juan@email.com",
    "password": "mipassword123"
  }'
```

#### 2. Obtener token de autenticación
```bash
curl -X POST http://127.0.0.1:8000/auth/token/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "juanperez",
    "password": "mipassword123"
  }'
```

#### 3. Ver el menú (sin autenticación)
```bash
curl -X GET http://127.0.0.1:8000/api/menu/
```

#### 4. Crear una nueva reserva (con token)
```bash
curl -X POST http://127.0.0.1:8000/api/bookings/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token tu_token_aqui" \
  -d '{
    "Name": "Juan Pérez",
    "No_of_guests": 4,
    "BookingDate": "2025-06-25T19:00:00Z"
  }'
```

#### 5. Obtener todas las reservas (con token)
```bash
curl -X GET http://127.0.0.1:8000/api/bookings/ \
  -H "Authorization: Token tu_token_aqui"
```

### 🧪 Pruebas con Insomnia/Postman

#### Configuración Inicial
1. **Base URL**: `http://127.0.0.1:8000`
2. **Content-Type**: `application/json` (para POST/PUT)
3. **Authorization**: `Token tu_token_aqui` (cuando sea requerido)

#### Flujo de Pruebas Recomendado
1. **Crear usuario**: `POST /auth/users/`
2. **Obtener token**: `POST /auth/token/login/`
3. **Ver menú**: `GET /api/menu/`
4. **Crear reserva**: `POST /api/bookings/`
5. **Ver reservas**: `GET /api/bookings/`

### 📋 Formatos de Datos

#### Usuario
```json
{
  "username": "usuario123",
  "email": "usuario@email.com",
  "password": "password123"
}
```

#### Elemento del Menú
```json
{
  "Title": "Pasta Carbonara",
  "Price": "15.99",
  "Inventory": 25
}
```

#### Reserva
```json
{
  "Name": "Juan Pérez",
  "No_of_guests": 4,
  "BookingDate": "2025-06-25T19:00:00Z"
}
```

### ⚠️ Notas Importantes

- **Tokens**: Los tokens no expiran automáticamente. Usa `/auth/token/logout/` para cerrar sesión.
- **Permisos**: Los administradores pueden gestionar usuarios y menú. Los usuarios autenticados pueden gestionar sus reservas.
- **Fechas**: Usa formato ISO 8601 para fechas (`YYYY-MM-DDTHH:MM:SSZ`).

## 🧪 Guía de Pruebas Completa

### 📋 Prerrequisitos para las Pruebas

1. **Servidor ejecutándose**: `python manage.py runserver`
2. **Herramientas recomendadas**: 
   - Insomnia, Postman, o cURL
   - PowerShell (Windows) o Terminal (macOS/Linux)

### 🚀 Pruebas Paso a Paso

#### **Paso 1: Crear un Usuario Regular**

**PowerShell:**
```powershell
$body = @{username="testuser"; email="test@example.com"; password="testpass123"} | ConvertTo-Json
Invoke-RestMethod -Uri "http://127.0.0.1:8000/auth/users/" -Method POST -Body $body -ContentType "application/json"
```

**cURL:**
```bash
curl -X POST http://127.0.0.1:8000/auth/users/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "email": "test@example.com", "password": "testpass123"}'
```

**Respuesta esperada:**
```json
{
  "email": "test@example.com",
  "username": "testuser"
}
```

#### **Paso 2: Obtener Token de Autenticación**

**PowerShell:**
```powershell
$loginBody = @{username="testuser"; password="testpass123"} | ConvertTo-Json
$tokenResponse = Invoke-RestMethod -Uri "http://127.0.0.1:8000/auth/token/login/" -Method POST -Body $loginBody -ContentType "application/json"
$token = $tokenResponse.auth_token
Write-Host "Tu token es: $token"
```

**cURL:**
```bash
curl -X POST http://127.0.0.1:8000/auth/token/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass123"}'
```

**Respuesta esperada:**
```json
{
  "auth_token": "a8977fc33f938db2dd1a8f7a01adb63602677bdd"
}
```

#### **Paso 3: Ver el Menú (Público)**

**PowerShell:**
```powershell
$menu = Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/menu/" -Method GET
$menu.results | Format-Table
```

**cURL:**
```bash
curl -X GET http://127.0.0.1:8000/api/menu/
```

#### **Paso 4: Crear una Reserva (Requiere Token)**

**PowerShell:**
```powershell
$headers = @{"Authorization" = "Token tu_token_aqui"}
$booking = @{Name="Juan Perez"; No_of_guests=4; BookingDate="2025-06-25T19:00:00Z"} | ConvertTo-Json
$result = Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/bookings/" -Method POST -Body $booking -ContentType "application/json" -Headers $headers
$result
```

**cURL:**
```bash
curl -X POST http://127.0.0.1:8000/api/bookings/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token tu_token_aqui" \
  -d '{"Name": "Juan Perez", "No_of_guests": 4, "BookingDate": "2025-06-25T19:00:00Z"}'
```

#### **Paso 5: Ver Todas las Reservas (Requiere Token)**

**PowerShell:**
```powershell
$bookings = Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/bookings/" -Method GET -Headers $headers
$bookings.results | Format-Table
```

**cURL:**
```bash
curl -X GET http://127.0.0.1:8000/api/bookings/ \
  -H "Authorization: Token tu_token_aqui"
```

#### **Paso 6: Modificar una Reserva**

**PowerShell:**
```powershell
$updatedBooking = @{Name="Juan Perez"; No_of_guests=5; BookingDate="2025-06-25T19:00:00Z"} | ConvertTo-Json
$updateResult = Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/bookings/1/" -Method PUT -Body $updatedBooking -ContentType "application/json" -Headers $headers
```

#### **Paso 7: Eliminar una Reserva**

**PowerShell:**
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/bookings/1/" -Method DELETE -Headers $headers
```

### 🔐 Pruebas de Seguridad

#### **Verificar que la Autenticación Funciona**

**1. Intentar acceder a reservas sin token:**
```powershell
# Esto debe fallar con "Authentication credentials were not provided"
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/bookings/" -Method GET
```

**2. Intentar usar un token falso:**
```powershell
# Esto debe fallar con "Invalid token"
$fakeHeaders = @{"Authorization" = "Token tokenfalso123"}
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/bookings/" -Method GET -Headers $fakeHeaders
```

### 👨‍💼 Funciones de Administrador

#### **Crear un Superusuario**
```bash
python manage.py createsuperuser
```

#### **Obtener Token de Admin y Gestionar Menú**

**PowerShell:**
```powershell
# 1. Obtener token de admin
$adminLogin = @{username="admin"; password="tu_password_admin"} | ConvertTo-Json
$adminToken = Invoke-RestMethod -Uri "http://127.0.0.1:8000/auth/token/login/" -Method POST -Body $adminLogin -ContentType "application/json"
$adminHeaders = @{"Authorization" = "Token $($adminToken.auth_token)"}

# 2. Crear elemento del menú
$menuItem = @{Title="Pasta Carbonara"; Price="15.99"; Inventory=25} | ConvertTo-Json
$result = Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/menu/" -Method POST -Body $menuItem -ContentType "application/json" -Headers $adminHeaders

# 3. Modificar elemento del menú
$updatedItem = @{Title="Pasta Carbonara"; Price="17.99"; Inventory=25} | ConvertTo-Json
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/menu/1/" -Method PUT -Body $updatedItem -ContentType "application/json" -Headers $adminHeaders

# 4. Eliminar elemento del menú
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/menu/1/" -Method DELETE -Headers $adminHeaders
```

### 🔍 Casos de Error Comunes

#### **1. Sin Autenticación**
```json
{"detail": "Authentication credentials were not provided."}
```
**Solución:** Agregar header `Authorization: Token tu_token`

#### **2. Token Inválido**
```json
{"detail": "Invalid token."}
```
**Solución:** Verificar que el token sea correcto y válido

#### **3. Sin Permisos**
```json
{"detail": "You do not have permission to perform this action."}
```
**Solución:** Usar cuenta de administrador para operaciones de menú

#### **4. Datos Inválidos**
```json
{"field_name": ["Este campo es requerido."]}
```
**Solución:** Verificar que todos los campos requeridos estén presentes

### 📊 Resultados de Prueba Exitosa

**Menú Final:**
```
id | Title           | Price | Inventory
---|-----------------|-------|----------
1  | Pasta Carbonara | 17.99 | 25
3  | Grilled Salmon  | 22.95 | 15
```

**Reservas Finales:**
```
id | Name            | No_of_guests | BookingDate
---|-----------------|--------------|------------------
1  | Juan Perez      | 5            | 2025-06-25T19:00:00Z
2  | Maria Rodriguez | 2            | 2025-06-26T20:30:00Z
```

### 🎯 Flujo de Trabajo Completo

1. **Registro** → Crear usuario regular
2. **Autenticación** → Obtener token
3. **Exploración** → Ver menú público
4. **Reserva** → Crear, ver, modificar reservas
5. **Administración** → (Solo admin) Gestionar menú y usuarios

### ✅ Verificación de Funcionalidad

- ✅ **Creación de usuarios**: Funciona correctamente
- ✅ **Autenticación por token**: Implementada y segura
- ✅ **Gestión de reservas**: CRUD completo para usuarios autenticados
- ✅ **Gestión de menú**: CRUD completo para administradores
- ✅ **Seguridad**: Endpoints protegidos correctamente
- ✅ **Permisos**: Roles diferenciados (usuario/admin)

## 🧪 Testing Automatizado

Para ejecutar las pruebas:

```bash
cd littlelemon
python manage.py test
```

## 📁 Estructura del Proyecto

```
LittleLemon/
├── README.md
├── LICENSE
├── requirements.txt
├── env/                          # Entorno virtual
│   ├── Scripts/
│   ├── Lib/
│   └── pyvenv.cfg
└── littlelemon/                  # Proyecto Django principal
    ├── manage.py
    ├── db.sqlite3
    ├── templates/
    │   └── index.html
    ├── tests/                    # Pruebas unitarias
    │   ├── __init__.py
    │   ├── test_models.py
    │   └── test_views.py
    ├── littlelemon/              # Configuración del proyecto
    │   ├── __init__.py
    │   ├── settings.py           # Configuración principal
    │   ├── urls.py               # URLs principales
    │   ├── wsgi.py
    │   └── asgi.py
    └── restaurant/               # App principal del restaurante
        ├── __init__.py
        ├── admin.py              # Configuración del admin
        ├── apps.py
        ├── models.py             # Modelos (Menu, Booking)
        ├── serializers.py        # Serializadores DRF
        ├── views.py              # Vistas de la API
        ├── urls.py               # URLs de la app
        ├── tests.py
        ├── migrations/           # Migraciones de base de datos
        └── static/               # Archivos estáticos
            ├── css/
            └── img/
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

- [x] ✅ **API RESTful básica** - Implementada completamente
- [x] ✅ **Autenticación por tokens** - Funcionando con Djoser
- [x] ✅ **Gestión de menús** - CRUD completo para administradores
- [x] ✅ **Sistema de reservas** - CRUD completo para usuarios autenticados
- [x] ✅ **Tests unitarios** - Modelos y vistas probados
- [x] ✅ **Seguridad y permisos** - Implementados y verificados
- [x] ✅ **Documentación completa** - README con ejemplos prácticos
- [ ] 🔄 **Frontend web** - Interfaz de usuario
- [ ] 🔄 **Notificaciones por email** - Confirmación de reservas
- [ ] 🔄 **API de pedidos** - Sistema de pedidos en línea
- [ ] 🔄 **Integración con pagos** - Stripe/PayPal
- [ ] 🔄 **Deployment en producción** - Docker + Heroku/AWS

---

⭐ Si este proyecto te ha sido útil, ¡no olvides darle una estrella!
