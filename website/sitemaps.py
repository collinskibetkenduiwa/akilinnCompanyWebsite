from django.contrib import sitemaps
from django.urls import reverse

class MainSitemap(sitemaps.Sitemap):
    priority = 1.0
    changefreq = 'monthly'

    def items(self):
        return ['home','about','projects','subsidiaries']

    def location(self, item):
        return reverse(item)
    
class SecondarySitemap(sitemaps.Sitemap):
    priority = 0.9
    changefreq = 'monthly'

    def items(self):
        return ['careers', 'contact',]

    def location(self, item):
        return reverse(item)
   