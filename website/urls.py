"""website URL Configuration

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
import os

from core.views import (PackagesView, PortfolioView, ProductsView,
                        ServicesView, SiteView, contact)
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('sudo/', admin.site.urls),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('', SiteView.as_view(), name='site'),
    path('contact/', contact, name='contact'),
    path('packages/', PackagesView.as_view(), name='packages'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('products/', ProductsView.as_view(), name='products'),
    path('services/', ServicesView.as_view(), name='services')
]

mode = os.environ.get("DJANGO_SETTINGS_MODULE").split(".")[-1]

if mode == "development":

    import debug_toolbar
    from django.conf.urls.static import static

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
