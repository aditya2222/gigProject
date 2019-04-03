from django.db import models


# Create your models here.


class PagesModel(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True)
    mainHeader = models.CharField(max_length=120, blank=True, null=True)
    subHeader = models.CharField(max_length=120, blank=True, null=True)
    Image1 = models.ImageField(blank=True, null=True)
    Image2 = models.ImageField(blank=True, null=True)
    Image3 = models.ImageField(blank=True, null=True)
    About = models.TextField(max_length=120, blank=True, null=True)
    Footer = models.TextField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.title
