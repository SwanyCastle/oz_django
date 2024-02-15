from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    age = models.PositiveIntegerField(null=True)
    gender = models.CharField(max_length=10)

    def __str__(self) -> str:
        return f"{self.name} / ({self.age})"