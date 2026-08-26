from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "priority",
        "completed",
        "created_at",
        "updated_at",
    )

    list_filer = (
        "priority",
        "completed"
    )

    search_fields = (
        "title",
        "description",
    )