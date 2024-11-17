from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=200)  # Hash passwords in real scenarios
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.username
