from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                   # Asosiy sahifa (home)
    path('food/', views.food_list, name='food_list'),    # Barcha taomlar ro'yxati
    path('food/<int:pk>/', views.food_detail, name='food_detail'),
    path('add/', views.add_food, name='add_food'),
    path('add_food_type/', views.add_food_type, name='add_food_type'),  # Yangi FoodType qo'shish
    path('edit/<int:pk>/', views.edit_food, name='edit_food'),
    path('delete/<int:pk>/', views.delete_food, name='delete_food'),
]