from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    content = models.CharField(max_length=200, help_text='登録したいタスクを入力してください(200文字以内)')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
