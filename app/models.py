from django.db import models


# Create your models here.


class PagesModel(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True)
    body = models.TextField(max_length=120, blank=True, null=True)
    Image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title

