from django.urls import path
from patientsapp.views import patientCreate,PatientList


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('patients/',patientCreate.as_view(),name='patient-add'),
    path('patientList/',PatientList,name='patient-list'),
    
    
    
]