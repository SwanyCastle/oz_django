from django.contrib import admin
from .models import Board

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', 'date', 'likes', 'content', 'created_at', 'updated_at', 'user')
    list_filter = ('date', 'writer')
    search_fields = ('title', 'content')
    ordering = ('-date',)
    readonly_fields = ('writer',)
    fieldsets = (
        (None, {'fields': ('title', 'content')}),
        ('추가 옵션', {'fields': ('writer', 'user', 'likes', 'reviews'), 'classes': ('collapse',)}),
    )
    list_per_page = 1

    actions = ('increment_likes',)

    def increment_likes(self, request, queryset):
        for board in queryset:
                board.likes += 1
                board.save()

    increment_likes.short_description = "선택된 게시글의 좋아요 수 증가"