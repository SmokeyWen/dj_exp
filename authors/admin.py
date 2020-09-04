from django.contrib import admin

# Register your models here.
from .models import Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Author, AuthorAdmin)