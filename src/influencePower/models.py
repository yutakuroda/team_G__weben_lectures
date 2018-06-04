from django.db import models
import datetime
from django.contrib.auth.models import User

class Influencer(User):
    influence_power = models.IntegerField(default=0)
    
class NormalUser(User):
    age = models.IntegerField(default=0)

class Comment(models.Model):
    name = models.CharField(max_length=255, blank=True)
    text = models.TextField()
    target = models.ForeignKey(Influencer, on_delete=models.CASCADE)
    def __str__(self):
        return self.name