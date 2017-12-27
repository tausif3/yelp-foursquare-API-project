from django.db import models
from django.conf import settings 

from django.db.models.signals import post_save
from django.dispatch import receiver



 # the name was intialised as 'yelp' but it contains data from both yelp and foursquare

class locate_model_yelp(models.Model): 
    city            =  models.CharField(max_length=120,null=True,blank=True)
    display_address =  models.CharField(max_length=120,null=True,blank=True)
    country         =  models.CharField(max_length=120,null=True,blank=True)
    state           =  models.CharField(max_length=120,null=True,blank=True)
    address1        =  models.CharField(max_length=120,null=True,blank=True)
    zip_code        =  models.IntegerField(null=True,blank=True)
    save_flag       =  models.BooleanField(default= False)
    venue           =  models.CharField(max_length=120,null=True,blank=True)
    api_used        =  models.CharField(max_length=10,null=True,blank=True)
   
    class Meta:
        verbose_name = 'database'
        verbose_name_plural = 'database'


    def __unicode__(self):
        return unicode(self.city) or u''




@receiver(post_save, sender = locate_model_yelp)
def update_save_flag(sender,instance, *args, **kwargs):
    
    locate_model_yelp.objects.update(save_flag= True)
    
    
    
