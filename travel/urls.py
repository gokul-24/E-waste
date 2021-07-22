"""test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('request',views.request,name="request"),
    path('login/',views.login,name="login"),
    path('login/signup',views.signup,name="signup"),
    path('login/login',views.login,name="login"),
    path('logout',views.logout,name="login"),
    path('destinations',views.destinations,name="destinations"),
    path('destinations1',views.destinations1,name="destinations1"),
    path('search',views.search,name="search"),
    path('searchseller',views.searchseller,name="searchsellers"),
    path('add',views.add,name="add"),
    path('displaypickup',views.displaypickup,name="display"),
    path('pickedup',views.pickedup,name="pickedup"),
    path('addToCart',views.addToCart,name="add to cart"),
    path('displaycart',views.displaycart,name="cart"),
    path('doro',views.doro,name="doro"),
    path('displayorder',views.displayorder,name="displayorder"),
    path('selling',views.selling,name="selling"),
    path('selling1',views.selling1,name="selling"),
    path('cancelorder',views.cancelorder,name="cancel"),
    path('confirm',views.confirm,name="confirm"),
    path('about',views.about,name="about"),
]
