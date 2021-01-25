from django.urls import path
from . import views



urlpatterns = [
    path('home/', views.user_details, name = 'admin_home'),
    path('delete/<username>', views.delete_user, name = 'delete_user'),
    path('', views.admin_login, name = 'admin_login'),
    path('logout/', views.admin_logout, name = 'admin_logout'),
    path('register/', views.user_register, name = 'user_registration'),
    path('edit/<str:username>', views.edit, name = 'edit_user')
    # path('search/', views.user_search, name = 'user_search')

]