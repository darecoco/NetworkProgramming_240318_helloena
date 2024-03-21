# helloena
***
1. startproject helloena
   1. python -m pip install django~=4.2 (4.2중 최신버전 설치)
   2. django-admin startproject _helloena_ .
   3. [python manage.py migrate]
   4. python manage.py runserver
2. startapp _playground_ 
   1. Terminal
      1. python manage.py startapp _playground_
   2. helloena/settings.py
      1. 'playground', in INSTALLED_APPS