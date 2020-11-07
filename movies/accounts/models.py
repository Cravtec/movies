from django.db import models
from django.contrib.auth.models import User
from django.db.models import TextField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = TextField()

    def __str__(self):
        return f'{self.user.username} Profile'
