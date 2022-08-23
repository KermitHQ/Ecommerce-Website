
from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import CustomAuthForm
from .views import registerView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='Account/login.html', authentication_form=CustomAuthForm), name = 'login'),
    path('register/', registerView, name = 'register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Account/logout.html'), name = 'logout'),
    
]
