from django.db import models
from django.conf import settings


class SavedSubmission(models.Model):
	"""Stores one submission's input and the generated recommendations."""
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
	raw_input = models.TextField(blank=True)
	results = models.TextField(help_text="Stored recommendations, newline-separated")
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["-created_at"]

	def __str__(self):
		return f"Submission {self.id} ({self.created_at:%Y-%m-%d %H:%M})"

