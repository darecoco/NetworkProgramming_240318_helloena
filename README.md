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
3. playground/
   - 정보 전달: urls -> views -> (models -> ) templates
   - 코드 작성: (models -> ) views -> templates -> urls
   1. views
      1. _say_hello()_
      2. _say_hello_html()_
   2. urls
      1. _playground/hello_ -> _say_hello()_
      2. _playground/hello_html_ -> _say_hello_html()_
   3. templates/playground/
      1. hello.html
4. helloena/
   1. urls, playground/urls
      1. _playground/_ -> _hello/_ -> _say_hello()_
      2. _playground/_ -> _hello_html/_ -> _say_hello_html()_