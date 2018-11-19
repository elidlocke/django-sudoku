from django.db import models

# Create your models here.
class Game(models.Model):
    creation_date = models.DateTimeField('date created')
    input = models.CharField(max_length=81)
    status = models.IntegerField(default=0)
    output = models.CharField(max_length=81, null=True, blank=True)
