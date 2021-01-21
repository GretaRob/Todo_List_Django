from django.db import models

# Create your models here.


class todo (models.Model):
    task = models.CharField(max_length=200, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.task)
