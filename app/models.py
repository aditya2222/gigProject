from django.db import models


# Create your models here.


class PagesModel(models.Model):
    headerTitle = models.CharField(max_length=120, blank=True, null=True)
    headingName1 = models.CharField(max_length=120, blank=True, null=True)
    p1Middle = models.CharField(max_length=120, blank=True, null=True)
    h2name2 = models.CharField(max_length=120, blank=True, null=True)
    h2more = models.CharField(max_length=120, blank=True, null=True)
    Link1Text = models.CharField(max_length=120, blank=True, null=True)
    Link2Text = models.CharField(max_length=120, blank=True, null=True)
    Link3Text = models.CharField(max_length=120, blank=True, null=True)
    Link4Text = models.CharField(max_length=120, blank=True, null=True)
    Link5Text = models.CharField(max_length=120, blank=True, null=True)
    Link6Text = models.CharField(max_length=120, blank=True, null=True)
    Link7Text = models.CharField(max_length=120, blank=True, null=True)
    Link8Text = models.CharField(max_length=120, blank=True, null=True)
    footerTitle = models.CharField(max_length=120, blank=True, null=True) 
    footerTitle2 = models.CharField(max_length=120, blank=True, null=True)


    def __str__(self):
        return self.headerTitle


class IndexModel(models.Model):
    indexTitle = models.CharField(max_length=120, blank=True, null=True)
    indexBodyHeader = models.CharField(max_length=120, blank=True, null=True)
    indexBodySubHeader = models.CharField(max_length=120, blank=True, null=True)
    idnexLeftHeader = models.CharField(max_length=120, blank=True, null=True)
    indexLeftHeaderContent = models.CharField(max_length=120, blank=True, null=True) 
    indexFeatured = models.CharField(max_length=120, blank=True, null=True)
    directLinkText1 = models.CharField(max_length=120, blank=True, null=True)
    directLinkText2 = models.CharField(max_length=120, blank=True, null=True)
    directLinkText3 = models.CharField(max_length=120, blank=True, null=True)
    directLinkText4 = models.CharField(max_length=120, blank=True, null=True)
    directLinkText5 = models.CharField(max_length=120, blank=True, null=True)
    directLinkText6 = models.CharField(max_length=120, blank=True, null=True)
    directLinkText7 = models.CharField(max_length=120, blank=True, null=True)
    directLinkText8 = models.CharField(max_length=120, blank=True, null=True)
    FooterTitle = models.CharField(max_length=120, blank=True, null=True)
    FooterTitle2 = models.CharField(max_length=120, blank=True, null=True)


    def __str__(self):
        return self.indexTitle
    

