"""loadapitest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from gpstracker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('couriers/<int:courier_id>/coordinates/get', views.get_courier_coordinates, name='get_courier_coordinates'),
    path('couriers/<int:courier_id>/coordinates/update', views.update_courier_coordinates, name='update_courier_coordinates'),
    # path('', views.fetch_actual_coordinates, name='home'),
]
