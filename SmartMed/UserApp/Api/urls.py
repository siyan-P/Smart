from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from UserApp.Api.views import registration_view

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('login/',obtain_auth_token,name='login'),
    path('register/',registration_view,name = 'register'),
]