from django.db import models
from django.utils.translation import gettext_lazy as _


class Media(models.Model):
    
    class MediaType(models.TextChoices):
        IMAGE = "image", _("Image")
        FILE = "file", _("File")
        MUSIC = "music", _("Music")
        VIDEO = "video", _("Video")

    file = models.FileField(_("File"), upload_to="files/")
    type = models.CharField(_("Type"), max_length=60, choices=MediaType.choices)

    def __str__(self):
        return self.id


class Settings(models.Model):
        home_image = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)
        home_title = models.CharField(_("Title"), max_length=120)
        home_subtitle = models.CharField(_("Subtitle"), max_length=120)

        def __str__(self):
            return self.home_title


        class Meta:
            verbose_name = _("Setting")
            verbose_name_plural = _("Settings")    


class Country(models.Model):
    name = models.CharField(_("Name"), max_length=120)
    code = models.CharField(_("Code"), max_length=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")    


class Region(models.Model):
    name = models.CharField(_("Name"), max_length=120)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="regions")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")


class OurInstagramStory(models.Model):
    image = models.ForeignKey(Media, on_delete=models.CASCADE, related_name="instagram_stories")
    story_link = models.URLField(_("Story link"), ) # Write validations for instagram stories

    def __str__(self):
        return f"Id: {self.id} |Link: {self.story_link}"    

    class Meta:
        verbose_name = _("Our instagram story")
        verbose_name_plural = _("Our instagram stories")


class CustomerFeedback(models.Model):
    description = models.TextField(_("Review"))
    rank = models.IntegerField(_("Rank"))
    customer_name = models.CharField(_("Customer Name"), max_length=80)
    customer_position = models.CharField(_("Customer Position"), max_length=60)
    customer_image = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True)
  
    def __str__(self):
        return self.customer_name

    class Meta:
        verbose_name = _("Customer feedback")
        verbose_name_plural = _("Customer feesbacks")




