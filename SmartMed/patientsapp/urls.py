from django.urls import path
from patientsapp.views import patientCreate,PatientList,update_nfc,patientInd


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('patients/',patientCreate.as_view(),name='patient-add'),
    path('patientList/',PatientList,name='patient-list'),
    path('patients-update/',update_nfc,name='update-add'),
    path('PatientInfo/<int:pk>/',patientInd.as_view(),name='listInd'),
    
    
    
]