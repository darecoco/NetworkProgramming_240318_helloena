"""
URL configuration for helloena project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 이러이러한 url로 들어오면 이러이러한 함수를 실행해!
    # 주의, 함수 적을 때 괄호 적으면 안 됨.
    path('playground/', include('playground.urls')),
    path('ENA/', include('ENA.urls')),
    # path('playground/hello/', playground.views.say_hello, name='playground_hello'),
    # path('playground/hello_html/', playground.views.say_hello_html, name='playground_hello_html'),
    path('admin/', admin.site.urls),
]
