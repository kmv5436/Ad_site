from django.shortcuts import render
from django.contrib.auth.views import LoginView 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView 
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import PasswordChangeView

from .models import AdvUser
from .forms import ProfileEditForm 

# Create your views here.

class BBLoginView(LoginView):
    template_name = 'main/login.html'

class BBLogoutView(LogoutView):
    pass 

def index(request):
    return render(request, 'main/index.html')

@login_required
def profile(request):
    return render(request, 'main/profile.html')

class ProfileEditView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = AdvUser
    template_name = 'main/profile_edit.html'
    form_class = ProfileEditForm
    success_url = reverse_lazy('main:profile')
    success_message = 'Данные пользователя изменены'
    
    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)
    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)

class PasswordEditView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    template_name = 'main/password_edit.html'
    success_url = reverse_lazy('main:profile')
    success_message = 'Пароль пользователя изменен'