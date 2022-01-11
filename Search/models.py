from django.db import models
from django.db.models.expressions import F

# Create your models here.
class SearchResult(models.Model):
    url = models.CharField(max_length=1000, blank=False, null=False)
    title = models.CharField(max_length=2000, blank=False, null=False)
    description = models.CharField(max_length=1500, blank=False, null=False)

    def __str__(self) -> str:
        return self.title

