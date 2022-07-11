"""django_practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from cats.views import index, get_cats, get_one_cat, create_cat, update_cat, delete_cat

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('index/', get_cats),
    path('index/new/', create_cat),
    path('index/<int:cat_id>/', get_one_cat),
    path('update/<int:cat_id>/', update_cat),
    path('delete/<int:cat_id>/', delete_cat),

]
