from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from doctors_app.views import login_doctor_view
from doctors_app.views import registration_view

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('login/',obtain_auth_token,name='login'),
    path('registerDr/',registration_view,name = 'register'),
    path('loginDr/',login_doctor_view,name = 'loginDr'),
]