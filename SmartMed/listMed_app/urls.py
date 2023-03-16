from django.urls import path
from listMed_app.views import MedicineView,UserPostListView,UserPostDeleteView


urlpatterns = [
    #path('admin/', admin.site.urls),
    
    path('medicineList/',MedicineView.as_view(),name = 'medicineList'),
    path('selectedMedicines/<int:user_id>/', UserPostListView.as_view(), name='user-post-list'),
    path('deleteMed/<int:pk>/',UserPostDeleteView.as_view(),name='medDelete')
    
]