from django.db import models


class Task(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item
