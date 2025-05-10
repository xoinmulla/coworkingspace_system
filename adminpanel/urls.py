from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

app_name = "adminpanel"  # ✅ Required for namespacing


urlpatterns = [
    path('dashboard/', views.dashboard, name='admin-dashboard'),
    path('spaces/', views.space_management, name='space-management'),
    path('bookings/', views.booking_management, name='booking-management'),
    path('reporting/', views.reporting, name='reporting'),
    path('adminpanel/register/', views.register, name='register'),
    path("login/", auth_views.LoginView.as_view(template_name="adminpanel/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
