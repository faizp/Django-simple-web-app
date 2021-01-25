from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('', views.my_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout')
]