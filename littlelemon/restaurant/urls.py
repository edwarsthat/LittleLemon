from django.contrib import admin 
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# ===========================================
# ROUTER PARA VIEWSETS
# ===========================================
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'bookings', views.BookingViewSet)
router.register(r'menu', views.MenuViewSet)
router.register(r'menu-readonly', views.MenuReadOnlyViewSet, basename='menu-readonly')

urlpatterns = [
    # Vista tradicional
    path('', views.index, name='index'),
    
    # ===========================================
    # VIEWSETS (Recomendado - Automático)
    # ===========================================
    path('api/', include(router.urls)),
    
    # ===========================================
    # FUNCTION-BASED VIEWS
    # ===========================================
    path('api/function/users/', views.user_list_function, name='user-list-function'),
    path('api/function/users/<int:pk>/', views.user_detail_function, name='user-detail-function'),
    
    # ===========================================
    # CLASS-BASED VIEWS (APIView)
    # ===========================================
    path('api/class/bookings/', views.BookingListAPIView.as_view(), name='booking-list-class'),
    path('api/class/bookings/<int:pk>/', views.BookingDetailAPIView.as_view(), name='booking-detail-class'),
    
    # ===========================================
    # MIXINS
    # ===========================================
    path('api/mixin/menu/', views.MenuListMixin.as_view(), name='menu-list-mixin'),
    path('api/mixin/menu/<int:pk>/', views.MenuDetailMixin.as_view(), name='menu-detail-mixin'),
    
    # ===========================================
    # GENERIC VIEWS  
    # ===========================================
    path('api/generic/users/', views.UserListGeneric.as_view(), name='user-list-generic'),
    path('api/generic/users/<int:pk>/', views.UserDetailGeneric.as_view(), name='user-detail-generic'),
    path('api/generic/bookings/', views.BookingListGeneric.as_view(), name='booking-list-generic'),
    path('api/generic/bookings/<int:pk>/', views.BookingDetailGeneric.as_view(), name='booking-detail-generic'),
]