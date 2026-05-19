from django.db import models

class SavedSubmission(models.Model):
    raw_input = models.TextField()
    results = models.TextField()  # 
    created_at = models.DateTimeField(auto_now_add=True)