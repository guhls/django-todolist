from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=60)
    is_completed = models.BooleanField(default=False)
    create_at = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self) -> str:
        return self.title
