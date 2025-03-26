from django.shortcuts import render
from django.contrib.auth.views import LoginView 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView 

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