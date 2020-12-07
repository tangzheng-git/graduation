"""graduation URL Configuration

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
from django.conf.urls import include, url
from personage import views
from django.conf.urls import url
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap

from django.contrib.sitemaps import views as sitemaps_views
from django.views.decorators.cache import cache_page
from personage.models import User

sitemaps = {
    'user': GenericSitemap({'queryset': User.objects.all(), 'date_field': 'pub_date'}, priority=0.6),
    # 如果还要加其它的可以模仿上面的
}

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path("", views.home),
    url(r'^personage/', include('personage.urls')),

]

urlpatterns += [
    url(r'^sitemap\.xml$', cache_page(86400)(sitemaps_views.index), {'sitemaps': sitemaps, 'sitemap_url_name': 'sitemaps'}),
    url(r'^sitemap-(?P<section>.+)\.xml$', cache_page(86400)(sitemaps_views.sitemap), {'sitemaps': sitemaps}, name='sitemaps'),
]