from django.db import models


# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length=45)
    means = models.TextField(default='Missing')
    type = models.TextField(default='Missing')

    def __str__(self):
        return self.word
