"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from post_app.views import home_page_view, PostView, CategoryView, PostDetailView, PostCreateView ,\
    CategoryDetailView

urlpatterns = [
    path('', home_page_view, name='home'),
    path('post', PostView.as_view(), name='post_view'),
    path('category', CategoryView.as_view(), name='category_view'),
    path('post/new', PostCreateView.as_view(), name='post-create'),
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail_view'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail_view'),
    path('admin/', admin.site.urls),
]
