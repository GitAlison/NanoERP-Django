from django.urls import path
from .views import *

app_name ='pedido'

urlpatterns =[
    #TODO Saidas
    path('saidas',Saidas.as_view(),name='saida-list'),
    path('nota-nova/', NotaCreate.as_view(), name='nota-create'),
    path('nota-update/<int:pk>', NotaUpdate.as_view(), name='nota-update'),
    path('nota-remove/<int:pk>', NotaRemove.as_view(), name='nota-delete'),


    # TODO Entradas
    path('entradas', Entradas.as_view(), name='entrada-list'),

    #TODO Remove Item
    path('remove-item-saida/<int:pk>',DeleteItemNota.as_view(),name='delete-item-nota'),

    #TODO Add Item
    path('add-item-nota/', AddItemNota.as_view(), name='add-item-nota'),

    #TODO Update Item
    path('update-item-nota/<int:pk>', UpdateItemNota.as_view(), name='update-item-nota'),

    # TODO Detail Nota
    path('nota-detail/<int:pk>',NotaDetail.as_view(),name='nota-detail'),
    # TODO Eventos Nota
    path('nota-concluir/<int:pk>',ConcluirNota.as_view(),name='concluir-nota'),
    path('nota-remover/<int:pk>', RemoverNota.as_view(), name='remover-nota')
]

