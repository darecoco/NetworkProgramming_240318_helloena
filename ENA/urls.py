from django.urls import path

from ENA import views

app_name = 'ENA'

urlpatterns = [
    path('character_list/', views.show_character_list, name='등장인물리스트'),
    path('<등장인물>/', views.show_character, name='등장인물'),
    # path('ena/', views.show_ena, name='ena'),
    # path('moony/', views.show_moony, name='moony'),
]