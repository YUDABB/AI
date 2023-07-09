from django.contrib import admin

# Register your models here.

from .models import Question
from .models import Answer

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question,QuestionAdmin)
#admin.site.register(Question)
#admin.site.register(QuestionAdmin)
admin.site.register(Answer)

