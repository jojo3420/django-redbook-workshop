from django.contrib import admin
from .models import Question
from .models import Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    # 필드 순서 변경
    # fields = ['pub_date', 'question_text']

    # 필드셋 개선
    fieldsets = [
        ('Question Statement', {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    # Choice model classs 와 같이 보기
    inlines = [ChoiceInline]

    # 레코드 리스트 컬럼 항목 지정 (화면에 보여지는 컬럼 목록)
    list_display = ('question_text', 'pub_date')
    # 필터 사이드 바 추가
    list_filter = ['pub_date']
    # 검색 박스 추가
    search_fields = ['question_text']


# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
