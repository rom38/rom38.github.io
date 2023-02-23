from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE,
        related_name='user_profile')
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    def __str__(self):
        return str(self.user)
