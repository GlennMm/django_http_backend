from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    interests = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Todo:
    pass
