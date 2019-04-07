from django.db import models


# Create your models here.


class PagesModel(models.Model):

    city = models.CharField(max_length=120, blank=True, null=True)
    title = models.CharField(max_length=120, blank=True, null=True)
    keywords = models.CharField(max_length=120, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    h2name1 = models.CharField(max_length=120, blank=True, null=True)
    p1middle = models.CharField(max_length=120, blank=True, null=True)
    p2middle = models.CharField(max_length=120, blank=True, null=True)
    h2name2 = models.CharField(max_length=120, blank=True, null=True)
    logolink = models.CharField(max_length=120, blank=True, null=True)
    logopath = models.ImageField(blank=True, null=True)
    logoalt = models.CharField(max_length=120, blank=True, null=True)
    primaryLink = models.CharField(max_length=120, blank=True, null=True)
    h4name = models.CharField(max_length=120, blank=True, null=True)
    phone = models.CharField(max_length=120, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    h2more = models.CharField(max_length=120, blank=True, null=True)
    link1 = models.CharField(max_length=120, blank=True, null=True)
    link2 = models.CharField(max_length=120, blank=True, null=True)
    link3 = models.CharField(max_length=120, blank=True, null=True)
    link4 = models.CharField(max_length=120, blank=True, null=True)
    link5 = models.CharField(max_length=120, blank=True, null=True)
    link6 = models.CharField(max_length=120, blank=True, null=True)
    link7 = models.CharField(max_length=120, blank=True, null=True)
    link8 = models.CharField(max_length=120, blank=True, null=True)
    link1text = models.CharField(max_length=120, blank=True, null=True)
    link2text = models.CharField(max_length=120, blank=True, null=True)
    link3text = models.CharField(max_length=120, blank=True, null=True)
    link4text = models.CharField(max_length=120, blank=True, null=True)
    link5text = models.CharField(max_length=120, blank=True, null=True)
    link6text = models.CharField(max_length=120, blank=True, null=True)
    link7text = models.CharField(max_length=120, blank=True, null=True)
    link8text = models.CharField(max_length=120, blank=True, null=True)

    footerTitle = models.CharField(max_length=120, blank=True, null=True)
    footerTitle2 = models.CharField(max_length=120, blank=True, null=True)
    footerp1 = models.CharField(max_length=120, blank=True, null=True)
    footerLink = models.CharField(max_length=120, blank=True, null=True)
    footerLinkText = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.title


class IndexModel(models.Model):
    indexTitle = models.CharField(max_length=50, null=True, blank=True)
    bannerImage = models.ImageField(blank=True, null=True)
    indexHeaderTitle = models.CharField(max_length=120, blank=True, null=True)
    indexBannerText = models.CharField(max_length=120, blank=True, null=True)
    indexBannerText2 = models.CharField(max_length=120, blank=True, null=True)
    indexLeftHeader = models.CharField(max_length=120, blank=True, null=True)
    indexLeftHeaderContent = models.CharField(
        max_length=120, blank=True, null=True)
    indexFeatured = models.CharField(max_length=120, blank=True, null=True)
    indexFeaturedLink = models.CharField(max_length=120, blank=True, null=True)
    indexFeaturedImage = models.ImageField(blank=True, null=True)
    indexFeaturedh4 = models.CharField(max_length=120, blank=True, null=True)
    indexFeaturedP = models.CharField(max_length=120, blank=True, null=True)
    indirectLink1 = models.CharField(max_length=120, null=True, blank=True)
    indirectLink1Text = models.CharField(max_length=120, null=True, blank=True)
    indirectLink2 = models.CharField(max_length=120, null=True, blank=True)
    indirectLink2Text = models.CharField(max_length=120, null=True, blank=True)
    indirectLink3 = models.CharField(max_length=120, null=True, blank=True)
    indirectLink3Text = models.CharField(max_length=120, null=True, blank=True)
    indirectLink4 = models.CharField(max_length=120, null=True, blank=True)
    indirectLink4Text = models.CharField(max_length=120, null=True, blank=True)
    indirectLink5 = models.CharField(max_length=120, null=True, blank=True)
    indirectLink5Text = models.CharField(max_length=120, null=True, blank=True)
    indirectLink6 = models.CharField(max_length=120, null=True, blank=True)
    indirectLink6Text = models.CharField(max_length=120, null=True, blank=True)
    indirectLink7 = models.CharField(max_length=120, null=True, blank=True)
    indirectLink7Text = models.CharField(max_length=120, null=True, blank=True)
    indirectLink8 = models.CharField(max_length=120, null=True, blank=True)
    indirectLink8text = models.CharField(max_length=120, null=True, blank=True)
    footerTitle = models.CharField(max_length=120, blank=True, null=True)
    footerTitle2 = models.CharField(max_length=120, blank=True, null=True)
    footerp1 = models.CharField(max_length=120, blank=True, null=True)
    footerLink = models.CharField(max_length=120, blank=True, null=True)
    footerLinkText = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.indexTitle
