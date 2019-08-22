from django.urls import path
from . import views

app_name='estoque'

urlpatterns = [
    # TODO url Estoque
    path('estoque', views.EstoqueCreate.as_view(), name='estoque'),
    path('estoques', views.EstoqueList.as_view(), name='estoque-list'),
    path('estoque-update/<int:pk>/', views.EstoqueUpdate.as_view(), name='estoque-update'),
]