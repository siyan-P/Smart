from django.urls import path
from listMed_app.views import MedicineView,UserPostListView,UserPostDeleteView,CaretakerMedicineView,HistoryView,history_view


urlpatterns = [
    #path('admin/', admin.site.urls),
    
    path('medicineList/',MedicineView.as_view(),name = 'medicineList'),
    path('selectedMedicines/', UserPostListView, name='user-post-list'),
    path('listedMed/', CaretakerMedicineView, name='user-post-list'),
    path('deleteMed/<int:pk>/',UserPostDeleteView.as_view(),name='medDelete'),
    path('HistoryView/',HistoryView,name='historyCaretaker'),
    path('history/',history_view,name = 'history'),
    
    
]