from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from UserApp.Api.views import registration_view,login_view
from UserApp.views import UserList,UserInd

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('login/',obtain_auth_token,name='login'),
    path('register/',registration_view,name = 'register'),
    path('login/',login_view,name = 'login'),
    path('listUsers/',UserList.as_view(),name='UserList'),
    path('listUsers/<int:pk>/',UserInd.as_view(),name='listInd'),
    
    
]