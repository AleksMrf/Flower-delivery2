from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog_home, name='catalog_home'),
    path('<int:flower_id>/', views.flower_detail, name='flower_detail'),
]