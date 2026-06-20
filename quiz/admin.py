from django.contrib import admin
from .models import Question, Result

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    # Admin panelda fanlar bo'yicha guruhlab ko'rsatish
    list_display = ('question_text', 'subject', 'correct_answer')
    list_filter = ('subject',)  # Yon tomonda fanlar bo'yicha filtr chiqadi
    search_fields = ('question_text',) # Savol matni bo'yicha qidirish

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'score', 'date')
    list_filter = ('date',)