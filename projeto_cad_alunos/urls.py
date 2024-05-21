

from django.urls import path
from app_cad_alunos import views

urlpatterns = [
    #rota, view responsavel, nome de referência. ex academiatal/alunos
    #alunos.com
    path('',views.home,name='home'), 
    #alunos.com/alunos
    path('alunos/',views.alunos,name='lista_alunos')
    ]
