from typing import Any
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Category(models.Model):
    Category_ID = models.AutoField(primary_key=True, editable=False)
    Category = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.Category


class Question(models.Model):
    Question_ID = models.AutoField(primary_key=True, editable=False)
    Question_Text = models.TextField()
    Category = models.ForeignKey(Category, default=False, on_delete=models.SET_DEFAULT)

    def __str__(self) -> str:
        if not self.Question_Text:
            raise ValueError("Der Fragetext darf nicht leer sein.")
        return self.Question_Text

class Answers(models.Model):
    Answers_ID = models.AutoField(primary_key=True, editable=False)
    Question = models.ForeignKey(Question, on_delete=models.CASCADE)
    Answer = models.CharField(max_length=255)
    Is_Correct = models.BooleanField(default = False)
    
    def __str__(self) -> str:
        return self.Answer
    
    def clean(self) -> None:
        question_answers = Answers.objects.filter(Question = self.Question).count()
        MAX_Answers = 4
        if question_answers >= MAX_Answers:
            raise ValidationError({"__all__": f"Es dürfen höchstens {MAX_Answers} Antworten erstellt werden."})
        super().clean() 
    
    def validate_unique(self, exclude: None) -> None:
        if self.Is_Correct:
            other_correct_answers = Answers.objects.filter(Question = self.Question, Is_Correct = True).exclude(pk=self.pk)
            if other_correct_answers.exists():
                raise ValidationError({"Is_Correct": ["Es kann nur eine Antwort richtig sein!"]})