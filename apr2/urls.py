"""
URL configuration for apr2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from apr2app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.Register.as_view(),name="register"),
    path('auth/login/',views.Token.as_view(),name="login"),
    path('shipment/post/',views.ShipmentPost.as_view(),name="shipmentpost"),
    path('api/search',views.Query.as_view(),name="seraching"),
    path('auth/api1/',views.Api1.as_view(),name="api1"),
    path('auth/update/<int:shipmentId>/',views.Api1.as_view(),name="api1"),
    path('auth/search/<int:shipmentId>/',views.Api1.as_view(),name="api1"),
    path('auth/delete/<int:shipmentId>/',views.Api1.as_view(),name="api1"),
]
