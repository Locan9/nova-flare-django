from django.contrib import admin
from .models import SavedSubmission

@admin.register(SavedSubmission)
class SavedSubmissionAdmin(admin.ModelAdmin):
    list_display = ['id', 'raw_input', 'created_at']