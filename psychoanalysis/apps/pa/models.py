from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Category(models.Model):
    DIRECT = 'd'
    INDIRECT = 'i'
    OTHER = 'o'
    GROUPING_CHOICES = (
        (DIRECT, 'Direct'),
        (INDIRECT, 'Indirect'),
        (OTHER, 'Other'),
    )
    description = models.CharField(max_length=200)
    # Ugly hack to be replaced with a tree-structured category capability
    # Potentially django-treebeard / other mptt implementation.
    grouping = models.CharField(
        max_length=15, choices=GROUPING_CHOICES, default=DIRECT
    )

    def __unicode__(self):
        return self.description

    class Meta:
        verbose_name_plural = "Categories"


class ReportingPeriod(models.Model):
    name = models.CharField(max_length=120)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    slots_per_hour = models.IntegerField()
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Activity(models.Model):
    category = models.ForeignKey(Category)
    description = models.CharField(max_length=200)

    def __unicode__(self):
        return self.description

    class Meta:
        verbose_name_plural = "Activities"


class ActivityEntry(models.Model):
    day = models.CharField(max_length=10)
    hour = models.IntegerField()
    slot = models.IntegerField()
    activity = models.ForeignKey(Activity)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __unicode__(self):
        return "{0} {1} - {2}/{3}".format(
            self.user,
            self.day,
            self.hour,
            self.slot
        )

    class Meta:
        verbose_name_plural = "Activity entries"


class Profession(models.Model):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name


class User(AbstractUser):
    profession = models.ForeignKey(Profession, blank=True, null=True)
