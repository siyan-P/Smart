from django.urls import path
from listMed_app.views import MedicineView,UserPostListView,UserPostDeleteView,CaretakerMedicineView,HistoryView,history_view,medicineInd,medicine_Update


urlpatterns = [
    #path('admin/', admin.site.urls),
    
    path('medicineList/',MedicineView.as_view(),name = 'medicineList'),
    path('selectedMedicines/', UserPostListView, name='user-post-list'),
    path('listedMed/', CaretakerMedicineView, name='user-post-list'),
    path('deleteMed/<int:pk>/',UserPostDeleteView.as_view(),name='medDelete'),
    path('HistoryView/',HistoryView,name='historyCaretaker'),
    path('history/',history_view,name = 'history'),
    path('medicineInfo/<int:pk>/',medicineInd.as_view(),name='oneMedicineInd'),
    path('medicineUpdate/<int:pk>/',medicine_Update.as_view(),name='update-medicine'),
    
    
]