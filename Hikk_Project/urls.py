"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
# from Hikk_App import views
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.base, name='base'),
#     path('', views.home, name='home'),
# ]

# urlpatterns += staticfiles_urlpatterns()
from django.contrib import admin
from django.urls import path
from Hikk_App import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home1', views.home, name='home1'),  # Maps to the home view
    path('base', views.base, name='base'),  # Maps to the base view
    path('about', views.about, name='about'),  
    path('myaccount', views.myaccount, name='myaccount'),
    path('orderstatus', views.orderstatus, name='orderstatus'),
    path('newproduct', views.newproduct, name='newproduct'),
    path('allproducts', views.allproducts, name='allproducts'),
     path('favourite', views.favourite, name='favourite'),
       path('contact', views.contact, name='contact'),
         path('faq', views.faq, name='faq'),
              path('checkout', views.checkout, name='checkout'),
]

urlpatterns += staticfiles_urlpatterns()
