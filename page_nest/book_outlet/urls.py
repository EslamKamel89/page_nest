from __future__ import annotations

from django.urls import URLPattern, path

from . import views

urlpatterns :list[URLPattern]= [
    path('' , views.index , name='home') ,
    path('<slug:slug>' , views.show , name='book_detail')

]
