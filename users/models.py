from django.db import models
from cloudinary.models import CloudinaryField
from django.db import models
from django.db import models
from  django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('images')
    bio = models.TextField(default="Hello there!")
    email = models.CharField(blank = True, max_length = 100)
    
    def __str__(self):
        return  f'{self.user.username}' 

    def save_profile(self):
        self.save()

    @classmethod
    def search_by_username (cls,search_term):
        return cls.objects.filter(user__username__icontains=search_term).all()   
        
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
