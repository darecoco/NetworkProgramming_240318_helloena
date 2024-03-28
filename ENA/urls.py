from django.urls import path

from ENA import views

app_name = 'ENA'

urlpatterns = [
    path('ena/', views.show_ena, name='ena'),  # {% url 'ENA:ena' %}
    path('moony/', views.show_moony, name='hello_html'),  # {% url 'ENA:moony' %}
]
