from django.contrib import admin
from .models import Quiz, Question, Choice, Answer

from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)
