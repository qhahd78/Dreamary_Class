from . import views
from django.urls import path

urlpatterns = [
    path('profile/<int:designer_id>', views.detail, name = "detail"),
    path('new/', views.new, name = "new"),
    path('', views.home, name='home'),
    path('introduce/', views.introduce, name = "introduce"),
    path('create/', views.create, name= "create"),
    path('delete/<int:designer_id>/', views.delete, name = "delete"),
]