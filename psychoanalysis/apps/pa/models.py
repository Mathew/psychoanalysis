from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms.models import model_to_dict


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

    def describe_self(self):
        data = {
            'description': self.description,
            'activities': [a.describe_self() for a in self.activity_set.all()]
        }
        return data

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

    def describe_categories(self):
        return [c.describe_self() for c in self.categories.all()]

    def retrieve_user_entries(self, user):
        # barf
        return ActivityEntry.objects.filter(
            user=user,
            activity__category__reportingperiod=self
        )

    def retrieve_user_entries_by_day(self, user, day):
        # barf
        return self.retrieve_user_entries(user).filter(day=day)

    def create_user_day_entries(self, user, day):
        # barf
        for x in xrange(8, 19):
            for y in xrange(1, self.slots_per_hour + 1):
                ActivityEntry.objects.get_or_create(day=day, user=user, hour=x, slot=y)


class Activity(models.Model):
    category = models.ForeignKey(Category)
    description = models.CharField(max_length=200)

    def describe_self(self):
        return {'description': self.description}

    def __unicode__(self):
        return self.description

    class Meta:
        verbose_name_plural = "Activities"


class ActivityEntry(models.Model):
    day = models.CharField(max_length=10)
    hour = models.IntegerField()
    slot = models.IntegerField()
    activity = models.ForeignKey(Activity, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __unicode__(self):
        return "{0} {1} - {2}/{3}".format(
            self.user,
            self.day,
            self.hour,
            self.slot
        )

    def to_dict(self):
        return model_to_dict(self, fields=['id', 'day', 'hour', 'slot', 'activity', 'user'])

    class Meta:
        verbose_name_plural = "Activity entries"


class Profession(models.Model):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name


class User(AbstractUser):
    profession = models.ForeignKey(Profession, blank=True, null=True)
