from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('store', views.store, name='store'),
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout, name='logout'),
    path('new', views.new, name='new')
]
