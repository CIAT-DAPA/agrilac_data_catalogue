from django.urls import path
from .views import InstitutionListView, InstitutionCreateView, InstitutionUpdateView, InstitutionDeleteView

urlpatterns = [
    path('', InstitutionListView.as_view(), name='institution_list'),
    path('create/', InstitutionCreateView.as_view(), name='institution_create'),
    path('update/<int:pk>/', InstitutionUpdateView.as_view(), name='institution_update'),
    path('institutions/<int:pk>/delete/', InstitutionDeleteView.as_view(), name='institution_delete'),

]