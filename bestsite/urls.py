"""bestsite URL Configuration

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
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from users.views import Registration
from users.views import CSV
from users.views import download_pdf
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('user/csv/download_my_pdf',download_pdf,name='download_my_pdf'),
    path('user/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='layout.html'), name='layout'),
    path('user/registration/', Registration.as_view(template_name = 'registration/registration.html'), name='registration'),
    path('user/csv/', CSV.as_view(template_name = 'csv.html'), name='csv')
]
