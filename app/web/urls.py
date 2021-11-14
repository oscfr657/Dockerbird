"""devweb URL Configuration

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
from django.urls import path, include, re_path

from django.contrib.sitemaps.views import sitemap

# Wagtail
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls

from wagtail.contrib.sitemaps import Sitemap


from django.conf import settings
from django.conf.urls.static import static

from birdapp657.views import search as search_view


admin.autodiscover()

SITEMAPS = {"wagtail": Sitemap}

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^sitemap\.xml$', sitemap, { 'sitemaps': SITEMAPS}),
    path('gallery657/', include('gallery657.urls', namespace='gallery657')),
  ]

urlpatterns += [
    path('search/', search_view),
    #  Wagtail
    re_path(r'^birdapp/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'', include(wagtail_urls)),
  ]

handler403 = 'birdapp657.views.bird_page_403'
handler404 = 'birdapp657.views.bird_page_404'
handler500 = 'birdapp657.views.bird_page_500'


if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
