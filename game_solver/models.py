from django.db import models
from datetime import datetime

# Create your models here.
class Game(models.Model):
    creation_date = models.DateTimeField('date created', default=datetime.now)
    input = models.CharField(max_length=81)
    output = models.CharField(max_length=81, null=True, blank=True)

    def __str__(self):
        return self.input
