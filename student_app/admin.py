from django.contrib import admin
from .models import *

# Register your models here.

class SchoolAdmin(admin.ModelAdmin):
   

    fieldsets = (
	    ('School data', {'fields': ('name','address','rating','email','contact_no','websit','enabled',)}),
	    ('Date', {'fields': ('created_date','modified_date',)}), 
	)
    search_fields = ('name',)
    ordering = ('-created_date',)
    list_display = ('name', 'rating')
    list_display_links = ('name', 'rating')
    list_filter = ('rating', )

class StudentAdmin(admin.ModelAdmin):
  

    search_fields = ('first_name',)
    ordering = ('-created_date',)
    list_display = ('roll_no','first_name','standard')
    list_display_links = ('roll_no','first_name')
    list_filter = ('standard', )

admin.site.register(School, SchoolAdmin)
admin.site.register(Student, StudentAdmin)