from django.urls import path
from .views import ProfileEditView
from .views import ProfileEditView, index
from .views import BBLoginView 
from .views import profile
from .views import BBLogoutView
from .views import PasswordEditView

app_name = 'main'
urlpatterns = [
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/password/edit/', PasswordEditView.as_view(), name='password_edit'),
    path('accounts/profile/edit/', ProfileEditView.as_view(), name='profile_edit'), 
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', BBLoginView.as_view(), name='login'), 
    path('', index, name='index'),
] 