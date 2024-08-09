from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Institution
from .forms import InstitutionCreationForm, InstitutionChangeForm

class InstitutionListView(ListView):
    model = Institution
    template_name = 'manage_institution/institution_list.html'

class InstitutionCreateView(CreateView):
    model = Institution
    form_class = InstitutionCreationForm
    template_name = 'manage_institution/institution_form.html'
    success_url = reverse_lazy('institution_list')

class InstitutionUpdateView(UpdateView):
    model = Institution
    form_class = InstitutionChangeForm
    template_name = 'manage_institution/institution_form.html'
    success_url = reverse_lazy('institution_list')
