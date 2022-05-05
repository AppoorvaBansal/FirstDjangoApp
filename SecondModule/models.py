from django.db import models


# Create your models here.
class UserData(models.Model):
    username=models.CharField(max_length=50,default="ABC")
    password=models.CharField(max_length=20)
    isAdmin=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.username + " "+ self.password + "  -"+ str(self.isAdmin)
