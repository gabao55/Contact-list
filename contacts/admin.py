from django.contrib import admin
from .models import Category, Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'telephone', 'email', 'category' ,'show')
    list_display_links = ('id', 'name', 'surname')
    # list_filter = ('name', 'surname')
    list_per_page = 10
    search_fields = ('name', 'surname', 'email')
    list_editable = ('telephone', 'show')

# Register your models here.
admin.site.register(Category)
admin.site.register(Contact, ContactAdmin)