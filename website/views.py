from django.shortcuts import render,redirect
from django.contrib import messages

from .models import Footer
from .models import About
from .models import Projects
from .models import Subsidiaries
from .models import Careers
from .models import User_Contact

def home_redirect(request):
    return redirect("home")
 
def home(request):
    contact_Querry = Footer.objects.all() 
    home           = "active"
    about          = "nav-item"
    services       = "nav-item"
    subsidiaries   = "nav-item"
    careers        = "nav-item"
    contact        = "nav-item"                
    return render(request,'index.html',{
                                    "contact_info"        : contact_Querry,
                                          #  active page status
                                    "home_status"         : home,
                                    "about_status"        : about,
                                    "services_status"     : services,
                                    "subsidiaries_status" : subsidiaries,
                                    "careers_status"      : careers,
                                    "contact_status"      : contact,
    })

def about(request):
    contact_Querry = Footer.objects.all() 
    about_Querry   = About.objects.all()   
    home           = "nav-item"
    about          = "active"
    services       = "nav-item"
    subsidiaries   = "nav-item"
    careers        = "nav-item"
    contact        = "nav-item"                 
    return render(request,'about.html',{
                                    "contact_info"          : contact_Querry,
                                    "subsidiaries_carousel" : about_Querry,
                                          #  active page status
                                    "home_status"           : home,
                                    "about_status"          : about,
                                    "services_status"       : services,
                                    "subsidiaries_status"   : subsidiaries,
                                    "careers_status"        : careers,
                                    "contact_status"        : contact,
    })

def projects(request): 
    projects_Querry = Projects.objects.all() 
    contact_Querry  = Footer.objects.all() 
       
    home            = "nav-item"
    about           = "nav-item"
    services        = "active"
    subsidiaries    = "nav-item"
    careers         = "nav-item"
    contact         = "nav-item"             
    return render(request,'projects.html',{
                                    "contact_info"        : contact_Querry,
                                    "projects"            : projects_Querry,
                                          #  active page status
                                    "home_status"         : home,
                                    "about_status"        : about,
                                    "services_status"     : services,
                                    "subsidiaries_status" : subsidiaries,
                                    "careers_status"      : careers,
                                    "contact_status"      : contact,
    })

def subsidiaries(request): 
    contact_Querry = Footer.objects.all() 
    subsidiaries_Querry = Subsidiaries.objects.all() 
     
    home           = "nav-item"
    about          = "nav-item"
    services       = "nav-item"
    subsidiaries   = "active"
    careers      = "nav-item"
    contact      = "nav-item"                
    return render(request,'subsidiaries.html',{
                                    "contact_info"        : contact_Querry,
                                    "subsidiaries"        : subsidiaries_Querry,
                                          #  active page status
                                    "home_status"         : home,
                                    "about_status"        : about,
                                    "services_status"     : services,
                                    "subsidiaries_status" : subsidiaries,
                                    "careers_status"      : careers,
                                    "contact_status"      : contact,
    })
    
def careers(request):
    contact_Querry= Footer.objects.all() 
    careers_Querry= Careers.objects.all() 
     
    home         = "nav-item"
    about        = "nav-item"
    services     = "nav-item"
    subsidiaries = "nav-item"
    careers      = "active"
    contact      = "nav-item"                
    return render(request,'careers.html',{
                                    "contact_info"        : contact_Querry,
                                    "careers"             : careers_Querry,
                                          #  active page status
                                    "home_status"         : home,
                                    "about_status"        : about,
                                    "services_status"     : services,
                                    "subsidiaries_status" : subsidiaries,
                                    "careers_status"      : careers,
                                    "contact_status"      : contact,
    })
    
def contact(request):
    if request.method == "POST":
          Name = request.POST["name"]
          Email = request.POST["email"]
          Message = request.POST["message"]
          
          user_contact = User_Contact(Name=Name,Email=Email,Message=Message)
          user_contact.save()
          messages.success(request, 'Message Sent,We will talk to you soon') 
          return redirect('/contact#form')
      
    contact_Querry= Footer.objects.all() 
    home         = "nav-item"
    about        = "nav-item"
    services     = "nav-item"
    subsidiaries = "nav-item"
    careers      = "nav-item"
    contact      = "active"                 
    return render(request,'contact.html',{
                                    "contact_info"        : contact_Querry,
                                          #  active page status
                                    "home_status"         : home,
                                    "about_status"        : about,
                                    "services_status"     : services,
                                    "subsidiaries_status" : subsidiaries,
                                    "careers_status"      : careers,
                                    "contact_status"      : contact,
    })

def Error404(request,exception=None):                 
    return render(request,'404.html',status = 400)

def Error500(request,exception=None):                 
    return render(request,'404.html',status = 500)