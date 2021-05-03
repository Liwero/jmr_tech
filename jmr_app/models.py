from django.db import models

class RedirectURL(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    original_url = models.URLField()

    def __str__(self):
        return f"{self.original_url} - Created at {self.created_date}"
