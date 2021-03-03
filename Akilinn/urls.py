"""Akilinn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import MainSitemap
from website.sitemaps import SecondarySitemap
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import (handler400, handler403, handler404, handler500)

sitemaps = {
    'main'      : MainSitemap,
    'secondary' : SecondarySitemap,
}
def trigger_error(request):
    division_by_zero = 1 / 0
urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'), #sitemaps
    # path('robots.txt', include('robots.urls')),#robotics
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('sentry-debug/', trigger_error),#sentry
    path('ckeditor/', include('ckeditor_uploader.urls')),#ckeditor
    path('robots\.txt', include('robots.urls')),
    
]
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
handler404 = 'website.views.Error404'#not found
handler500 = 'website.views.Error500'#server error
