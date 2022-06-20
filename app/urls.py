from django.urls import path
from . import views
from . import views as user_views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', user_views.update_profile, name='update_profile'),
]