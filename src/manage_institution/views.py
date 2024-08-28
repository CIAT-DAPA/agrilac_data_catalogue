from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Institution
from .forms import InstitutionCreationForm, InstitutionChangeForm
from django.contrib import messages
from usermanagement.models import CustomUser as User


class InstitutionListView(ListView):
    model = Institution
    template_name = 'manage_institution/institution_list.html'
    
    def get_queryset(self):
        return Institution.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['institutions'] = self.get_queryset()
        return context

class InstitutionCreateView(CreateView):
    model = Institution
    form_class = InstitutionCreationForm
    template_name = 'manage_institution/institution_form.html'
    success_url = reverse_lazy('institution_list')

    def form_valid(self, form):
        print("Formulario es válido, datos: ", form.cleaned_data)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("Formulario es inválido. Errores:", form.errors)
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['owners'] = User.objects.all()  # Agregar lista de usuarios al contexto
        return context

class InstitutionUpdateView(UpdateView):
    model = Institution
    form_class = InstitutionChangeForm
    template_name = 'manage_institution/institution_form.html'
    success_url = reverse_lazy('institution_list')

    def form_valid(self, form):
        messages.success(self.request, "Los cambios se han guardado exitosamente.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['owners'] = User.objects.all()  # Asegúrate de que 'User' es el modelo correcto
        return context

class InstitutionDeleteView(DeleteView):
    model = Institution
    template_name = 'manage_institution/institution_confirm_delete.html'
    success_url = reverse_lazy('institution_list')