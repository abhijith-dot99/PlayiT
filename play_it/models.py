from django.db import models

# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=50, unique=True)
    guestcanpause = models.BooleanField(null=False, default=False)
    votestoskip = models.IntegerField(null=False, default=1)
    created = models.DateField(auto_now_add=False)

