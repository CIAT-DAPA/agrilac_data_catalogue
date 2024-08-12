from django.urls import path
from .views import InstitutionListView, InstitutionCreateView, InstitutionUpdateView

urlpatterns = [
    path('', InstitutionListView.as_view(), name='institution_list'),
    path('create/', InstitutionCreateView.as_view(), name='institution_create'),
    path('update/<int:pk>/', InstitutionUpdateView.as_view(), name='institution_update'),
]