from django.db import models


class Example(models.Model):
    title = models.CharField(max_length=150)
    descriptions = models.CharField(max_length=300, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
