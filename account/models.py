from django.db import models

# Create your models here.
class UserProfile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, unique=True)


    def __str__(self):
        return self.phone