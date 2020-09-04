from django.contrib import admin

# Register your models here.
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'complete_date', 'initial_price')
    list_display_links = ('id', 'title')
    list_filter = ('author',)
    search_fields = ('title', )

admin.site.register(Listing, ListingAdmin)