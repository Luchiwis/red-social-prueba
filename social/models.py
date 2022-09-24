from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=CASCADE)
    image = models.ImageField(default='batman.png', upload_to='profile_pics')

    def __str__(self):
        return f"perfil de {self.user.username}"
    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, related_name="posts")
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.user.username} : {self.content}"
