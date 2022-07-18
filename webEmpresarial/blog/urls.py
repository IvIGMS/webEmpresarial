from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    # Los nombres dinamicos del path son siempre cadenas de caracteres. Hay que forzarlo a int
    path('category/<int:category_id>/', views.category, name='category'),
]