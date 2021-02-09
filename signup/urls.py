from django.urls import path, include
from . import views



urlpatterns = [
    path('',views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('accounts/login/',views.login, name='login'),
    path('accounts/logout/', views.logout, name='logout'),
]