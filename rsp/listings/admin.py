from django.contrib import admin

# Register your models here.

from .models import Listing

#Change Viewing Data on Django Admin Panel
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor','is_published')
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25



#Register Model Class
admin.site.register(Listing, ListingAdmin)
