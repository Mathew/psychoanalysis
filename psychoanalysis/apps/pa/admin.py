from django.contrib import admin

from models import (
    ReportingPeriod, Category, Activity,
    ActivityEntry, Participant, Profession
)

models_tuple = (
    ReportingPeriod, Category, Activity,
    ActivityEntry, Participant, Profession
)

for m in models_tuple:
    admin.site.register(m)
