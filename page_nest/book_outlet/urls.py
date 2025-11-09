from __future__ import annotations

from django.urls import URLPattern, path

from . import views

urlpatterns :list[URLPattern]= [
    path('' , views.index , name='home') ,
    path('<int:id>' , views.show , name='show_book')

]
