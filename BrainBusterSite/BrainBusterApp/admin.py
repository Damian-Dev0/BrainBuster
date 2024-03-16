from typing import Any
from django.contrib import admin, messages
from .models import Question, Answers

# Register your models here.
admin.site.register(Question)
admin.site.register(Answers)