from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class account_profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    id_user=models.IntegerField()
    bio=models.TextField(max_length=100,blank=True)
    profile_image=models.ImageField(upload_to='profile_image',default="blank-profile_image")
    location=models.CharField(max_length=100,blank=True)

    def __str__(self) -> str:
        return self.user.username