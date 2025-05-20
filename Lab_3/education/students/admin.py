from django.contrib import admin
from .models import stud_list

@admin.register(stud_list)
class StudListAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'grade1', 'grade2', 'grade3', 'grade4', 'grade5')
