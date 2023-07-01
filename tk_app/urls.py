from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/',views.signup, name='signup'),
    path('login/',views.login ,name = 'login'),
    path('logout/',views.logout, name='logout'),
    path('add_crop/',views.add_crop, name ='add_crop'),
    path('current_user/',views.current_user, name ='current_user'),
    path('data_filter/',views.data_filter, name ='current_user'),
]
