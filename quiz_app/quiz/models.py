from django.db import models

# Create your models here.
class Quiz(models.Model):
    code = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=50)

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    text = models.TextField(max_length=200)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=50)
    is_correct = models.BooleanField(default=False)