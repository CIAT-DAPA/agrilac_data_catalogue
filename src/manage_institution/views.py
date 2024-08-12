from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Institution
from .forms import InstitutionCreationForm, InstitutionChangeForm
from django.contrib import messages


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

    def form_valid(self, form):
        messages.success(self.request, "Los cambios se han guardado exitosamente.")
        return super().form_valid(form)
