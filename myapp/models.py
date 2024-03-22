from django.db import models

class Goal(models.Model):
    subject = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.subject
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class User0322(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    displayname = models.CharField(max_length=100)

class TestTarget(models.Model):
    target_id = models.CharField(primary_key=True, max_length=255)
    user_id = models.CharField(max_length=100)
    content = models.CharField(max_length=255)

class TestTodo(models.Model):
    todo_id = models.CharField(primary_key=True, max_length=255)
    target_id = models.CharField(max_length=255)
    content = models.CharField(max_length=255)