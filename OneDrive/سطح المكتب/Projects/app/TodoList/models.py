from distutils.command.clean import clean
from django.db import models

# Create your models here.
class Base(models.Model):
    task = models.CharField(max_length=1000)
    completed= models.BooleanField(default=False)

    def __str__(self):
        return self.task + ' | ' + str(self.completed)




