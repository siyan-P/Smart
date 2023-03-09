from django.urls import path
from listMed_app.views import MedicineView


urlpatterns = [
    #path('admin/', admin.site.urls),
    
    path('medicineList/',MedicineView.as_view(),name = 'medicineList'),
    
]