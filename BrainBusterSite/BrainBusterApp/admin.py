from typing import Any
from django.contrib import admin, messages
from .models import Question, Answers, Category, Score

# Register your models here.
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Answers)
admin.site.register(Score)