from django.contrib import admin
from .models import SavedSubmission


@admin.register(SavedSubmission)
class SavedSubmissionAdmin(admin.ModelAdmin):
	list_display = ("id", "user", "created_at")
	search_fields = ("raw_input", "results")
	list_filter = ("created_at",)
