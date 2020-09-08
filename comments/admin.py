from django.contrib import admin
from .models import Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'listing_id', 'date')
    list_display_links = ('id', 'title', 'listing_id')
    search_fields = ('title', 'listing_id')
    list_per_page = 25


admin.site.register(Comment, CommentAdmin)