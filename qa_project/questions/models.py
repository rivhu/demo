from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.text

# Create your models here.
