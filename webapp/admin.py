from django.contrib import admin

# Register your models here.

from webapp.models import Task

class TasksAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_display_links = ['title']
    list_filter = ['status']
    search_fields = ['description']
    fields = ['description', 'status', 'completion_date', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']

admin.site.register(Task, TasksAdmin)