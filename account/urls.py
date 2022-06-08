from django.urls import path
from .views import RegistrationView, LoginView, LogautView

app_name = 'account'


urlpatterns = [
    path('registration/', RegistrationView, name="registration"),
    path('login/', LoginView, name="login"),
    path('logout/', LogautView, name="logout")
]