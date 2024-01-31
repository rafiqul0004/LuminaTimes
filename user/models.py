from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Viewer(models.Model):
    User = models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='user/images/')
    mobile_no=models.CharField(max_length=12)

    def __str__(self) -> str:
        return f'{self.User.first_name} {self.User.last_name}'
    
class Editor(models.Model):
    User = models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='user/images/')
    mobile_no=models.CharField(max_length=12)

    def __str__(self) -> str:
        return f'{self.User.first_name} {self.User.last_name}'