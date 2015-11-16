from django.contrib import admin

from .models import Question, Choice, Subscriber, List



# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


#Register the models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Subscriber)
admin.site.register(List)
