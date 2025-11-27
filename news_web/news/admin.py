from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_latest')
    list_filter = ('is_latest', 'created_at')
    search_fields = ('title', 'summary', 'content')