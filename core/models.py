from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone
# Create your models here.
class Profile(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    user_id = models.IntegerField()
    biography = models.TextField(blank=True)
    profile_img = models.ImageField(upload_to = 'profile_images',default = 'blank pic.png')
    location = models.CharField(max_length=100,blank=True)
    slug = models.SlugField(default=username)

    def __str__(self):
        return self.username.username


class Post(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    user = models.CharField(max_length=100)
    caption = models.TextField(blank=True)
    image = models.ImageField(upload_to='post_images')
    created_at = models.DateTimeField(default=timezone.now)
    no_likes = models.IntegerField(default=0)
 

    def __str__(self):
        return self.user
    
class Like(models.Model):
    post_id = models.CharField(max_length=40)
    username= models.CharField(max_length=70)

    def __str__(self):
        return self.username
    

