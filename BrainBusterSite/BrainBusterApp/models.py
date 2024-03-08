from django.db import models

# Create your models here.

class Question(models.Model):
    Question_ID = models.AutoField(primary_key=True, editable=False)
    Question_Text = models.TextField()
    
    def __str__(self) -> str:
        return self.Question_Text

class Answers(models.Model):
    Answers_ID = models.AutoField(primary_key=True, editable=False)
    Question = models.ForeignKey(Question, on_delete=models.CASCADE)
    Answer = models.CharField(max_length=255)
    Is_Correct = models.BooleanField()
    
    def __str__(self) -> str:
        return self.Answer
    
    
