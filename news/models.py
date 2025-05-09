from django.contrib.auth.models import AbstractUser
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Redactor(AbstractUser):
    years_of_experience = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    publishers = models.ManyToManyField(Redactor, )

    def __str__(self):
        return f"{self.title} ({self.published_date})"

