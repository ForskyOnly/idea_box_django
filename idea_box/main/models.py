from django.contrib.auth.models import User
from django.db import models

class Idea(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField(max_length=350)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    good = models.IntegerField(default=0)
    bad = models.IntegerField(default=0)

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    vote = models.CharField(max_length=10, choices=[("UP", "good"), ("DOWN", "bad")])
