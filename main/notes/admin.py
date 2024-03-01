from django.contrib import admin
from notes.models import Notes

# Register your models here.
class NotesAdmin(admin.ModelAdmin):
    list_listview=('note_name','note_description')
admin.site.register(Notes,NotesAdmin)