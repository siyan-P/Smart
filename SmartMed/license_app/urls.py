from license_app import views
from django.urls import path
from license_app.views import registration_view

urlpatterns = [
    path('licenseReg/',registration_view,name = 'register'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
]