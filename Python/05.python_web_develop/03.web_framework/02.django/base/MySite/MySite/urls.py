"""MySite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from 02.django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from . import views, mysite_db, search, search_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/", views.hello),
    path("mysitedb/", mysite_db.mysitedb),
    path("search-form/", search.search_form),
    path("search/", search.search),
    path("search-post/", search_post.search_post),
]
