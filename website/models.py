from django.db import models
from ckeditor.fields import RichTextField


class Footer(models.Model):
    ######################################
    #making table ony have one record
    def save(self,*args, **kwargs):
        if not self.pk and Footer.objects.exists():
            Footer.objects.all().delete()
        return super(Footer,self).save(*args, **kwargs)
    #####################################
    Email     = models.CharField(max_length=45,blank=True, )
    Post_Box  = models.CharField(max_length=45,blank=True, )
    Phone     = models.CharField(max_length=45,blank=True, )
    Facebook  = models.CharField(max_length=145,blank=True, )
    Twitter   = models.CharField(max_length=145,blank=True, )
    Instagram = models.CharField(max_length=145,blank=True, )
    LinkedIn  = models.CharField(max_length=145,blank=True, )
    Address   = RichTextField()
    class Meta:
        db_table = "Footer"
        verbose_name = u'Footer Section'
        
class About(models.Model):
    #####################################
    Image = models.ImageField( upload_to='home',)
    Name   = models.CharField(max_length=145,blank=True, )
    About   = models.CharField(max_length=145,blank=True, )
    Facebook  = models.CharField(max_length=145,blank=True, )
    Twitter   = models.CharField(max_length=145,blank=True, )
    Instagram = models.CharField(max_length=145,blank=True, )
    
    class Meta:
        db_table = "About"
        verbose_name = u'Subsidiaries  Section'
        
class Careers(models.Model):
    Body= RichTextField()  
    class Meta:
        db_table = "Careers"
        verbose_name = u'Career Body section'

class Projects(models.Model):
    Image =models.ImageField( upload_to='projects')
    Name  = models.CharField( max_length=50)
    Url   = models.CharField( max_length=50)
    class Meta:
        db_table = "Projects"
        verbose_name = u'Project'
        
class Subsidiaries(models.Model):
    Image =models.ImageField( upload_to='projects')
    Name = models.CharField( max_length=50)
    Url = models.CharField( max_length=50)
    class Meta:
        db_table = "Subsidiaries"
        verbose_name = u'Subsidiaries'
        
class User_Contact(models.Model):
    Name      = models.CharField( max_length = 50)
    Email     = models.CharField( max_length = 50)
    Message   = models.CharField( max_length = 50)
    Time      = models.TimeField( auto_now=True)
    Notes     = models.TextField()
    Contacted = models.BooleanField(default=False)
    
    class Meta:
        db_table = "User_Contact"
        verbose_name = u'Web user contact'
        verbose_name = u'Web users contacts'