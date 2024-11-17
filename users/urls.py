from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_users, name='get_users'),               # GET all users
    path('<int:pk>/', views.get_user, name='get_user'),         # GET single user
    path('create/', views.create_user, name='create_user'),     # POST create user
    path('update/<int:pk>/', views.update_user, name='update_user'),  # PUT update user
    path('delete/<int:pk>/', views.delete_user, name='delete_user'),  # DELETE user
]
