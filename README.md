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
      3. _say_bye_html()_
      4. -> templates에 context 전달
   2. urls
      1. _playground/hello_ -> _say_hello()_
      2. _playground/hello_html_ -> _say_hello_html()_
   3. templates/playground/
      1. hello.html
      2. bye.html
4. helloena/
   1. urls, playground/urls
      1. _playground/_ -> _hello/_ -> _say_hello()_
      2. _playground/_ -> _hello_html/_ -> _say_hello_html()_
      3. _playground/_ -> _bye_html/_ -> _say_bye_html()_
***
5. stratapp ENA
   1. Termianl
      1. python manage.py startapp ENA
   2. helloena/settings.py
      1. 'ENA', in INSTALLED_APPS
6. ENA
   1. views
      1. ~~show_ena()~~
      2. ~~show_moony()~~
      3. -> templates에 context 전달
      4. 정보를 하나로 묶고, 거기에서 꺼내오자
      5. show_character()
      6. image link -> image file(static)
      7. show_character_list
   2. templates/ENA/
      1. ~~ena.html~~
         1. title : Joel G - ENA
         2. h1 : ENA
         3. h2 : ena
         4. img : ena 사진
            1. border-radius : 50%
      2. ~~moony.html~~
      3. 등장인물.html
         1. group_name, name, img_src
         2. `{% load static %} <img src="{% img src %}">`
         3. character_list.html
   3. urls
      1. ~~ENA/ -> ena/ -> show_ena()~~
      2. ~~ENA/ -> moony/ -> show_moony()~~
      3. `ENA/ -> <character>/ -> show_character(character)`
      4. ENA/ -> character_list/ -> show_charactor_list()
   4. static/ENA/images/
      1. May I help you sir.gif, merci.png, moony.webp