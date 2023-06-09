"""
URL configuration for config project.

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
from blog import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from blog.views import CustomLoginView, some_view, save_bbcode, upload_file, subjects_students
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('create/', views.CreateItemView.as_view(), name='create'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logget_out.html'), name='logout'),
    path('some_view/', some_view, name='some_view'),
    path('contact/', views.contacts, name='contacts'),
    path('save_bbcode/', save_bbcode, name='save_bbcode'),
    path('upload/', upload_file, name='upload_file'),
    path('todo/', include('to_do.urls')),
    path('subjects_students/', subjects_students, name='subjects_students'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
