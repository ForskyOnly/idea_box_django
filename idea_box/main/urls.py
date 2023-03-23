from django.urls import path 
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.home_page, name='home'),
    path('signup/', views.SignupPage.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('', LogoutView.as_view(), name='logout'),
]
