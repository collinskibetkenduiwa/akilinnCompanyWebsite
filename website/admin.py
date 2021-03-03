from django.contrib import admin
from .models import Footer
from .models import About
from .models import Careers
from .models import Projects
from .models import Subsidiaries
from .models import User_Contact

admin.site.site_header='Akilinn Dashboard'
admin.site.site_header='The Akilinn'
admin.site.site_title ='Akilinn'
admin.site.index_title='Akilinn Admin'

class Contacts(admin.ModelAdmin):
    readonly_fields=['Name','Email','Message']
    list_display= ['Name','Email','Message','Contacted']
    search_fields = ['Name', 'Email',]
    ordering = ('Time',) 
    list_per_page = 30 
    
admin.site.register(About)
admin.site.register(Footer)
admin.site.register(Careers)
admin.site.register(Projects)
admin.site.register(Subsidiaries)
admin.site.register(User_Contact,Contacts)


