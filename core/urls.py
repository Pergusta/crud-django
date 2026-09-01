from django.urls import path
from . import views

urlpatterns = [
    path('', views.filme_list, name='filme_list'),
    path('novo/', views.filme_create, name='filme_create'),
    path('<int:pk>/', views.filme_detail, name='filme_detail'),
    path('<int:pk>/editar/', views.filme_update, name='filme_update'),
    path('<int:pk>/excluir/', views.filme_delete, name='filme_delete'),
]
