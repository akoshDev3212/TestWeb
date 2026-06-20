from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_score = models.IntegerField(default=0)
    level = models.CharField(max_length=50, default="Junior") # Junior, Middle, Senior
    
    def __str__(self):
        return f"{self.user.username} - {self.level}"

# Question modeliga qiyinchilik darajasini qo'shamiz
class Question(models.Model):
    DIFFICULTY_CHOICES = [('Easy', 'Oson'), ('Medium', 'O\'rtacha'), ('Hard', 'Qiyin')]
    subject = models.CharField(max_length=10)
    question_text = models.CharField(max_length=200)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='Easy')

    def __str__(self):
        return self.question_text
    
# Natijalar modeli
class Result(models.Model):
    user_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50) # Qaysi fandan topshirdi?
    score = models.IntegerField()
    total_questions = models.IntegerField() # Jami savollar soni
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} | {self.category} | {self.score}/{self.total_questions}"  
    