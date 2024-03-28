from django.urls import path

from ENA import views

app_name = 'ENA'

urlpatterns = [
    path('ena/', views.show_ena, name='ena'),
    path('moony/', views.show_moony, name='moony'),
]