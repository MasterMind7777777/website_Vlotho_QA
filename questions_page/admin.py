from django.contrib import admin
from .models import Question, Image

# Register your models here.
class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]