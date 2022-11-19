from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=CASCADE)
    image = models.ImageField(default='batman.png', upload_to='profile_pics')

    def __str__(self):
        return f"perfil de {self.user.username}"
    
class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
	timestamp = models.DateTimeField(default=timezone.now)
	content = models.TextField()
	likes = models.ManyToManyField(User, related_name='post_likes')
	dislikes = models.ManyToManyField(User, related_name='post_dislikes')

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return f'{self.user.username}: {self.content}'